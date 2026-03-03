from app.model.game_objects import ScrabbleBoard, LetterBag
from app.model.move_finder import MoveFinder
from app.model.types import (
    Cell, CellType, CellState, Tile, ValidationFlags, 
    ValidationResult, FormedWords, FormedWord, 
    TilePlacement, Move, MoveResult, AnchorCell,
    CellRestriction, GameState
)
from app.model.constants import (
    BOARD_SIZE, LETTER_SCORES, RACK_SLOTS, JOKER_CHAR,
    BINGO_BONUS
)
from app.model.word_structures import Trie, DICTIONARY


class ScrabbleModel:
    """Encapsulates game state and Scrabble rules."""

    def __init__(self) -> None:
        # Default game state
        self._players_turn: bool = True
        self._turn: int = 0
        self._player_points: int = 0
        self._bot_points: int = 0
        self._player_rack: list[Tile] = []
        self._bot_rack: list[Tile] = []
        self._board = ScrabbleBoard()
        self._letter_bag = LetterBag()

        # Logicall objects
        self._trie = Trie()
        self._move_processor = MoveProcessor(
            self._board, self._trie
        )
        self._restrictor = BoardRestrictor(
            self._board, self._trie, self._move_processor
        )
        self._move_finder = MoveFinder(
            self._board, self._trie, self._move_processor
        )

    @property
    def board(self) -> ScrabbleBoard:
        return self._board

    @property
    def turn(self) -> int:
        return self._turn
    
    @property
    def player_rack(self) -> list[Tile]:
        return self._player_rack

    @property
    def bot_rack(self) -> list[Tile]:
        return self._bot_rack
    
    @property
    def game_state(self) -> GameState:
        return GameState(
            player_points=self._player_points,
            bot_points=self._bot_points,
            remaining_tiles=(
                self._letter_bag.remaining_tiles
            ),
            turn=self._turn
        )

    def skip(self) -> None:
        self._turn += 1

    def select_tiles(self, selections: int) -> list[Tile]:
        return self._letter_bag.select(selections)

    def get_definition(self, word: str) -> str | None:
        return DICTIONARY.get(word, None)

    def update_rack(
            self, players: bool, new_tiles: list[Tile], 
            used_tiles: list[Tile] | None = None
        ) -> None:
        """
        Removes used tiles from move maker's rack and 
        adds new tiles.
        """
        if used_tiles:
            self._remove_used_tiles(players, used_tiles)

        if players:
            self._player_rack.extend(new_tiles)
        else:
            self._bot_rack.extend(new_tiles)
    
    def _remove_used_tiles(
            self, players: bool, tiles: list[Tile]
        ) -> None:
        """Removes used tiles from corresponding letter rack."""
        new_rack = (
            self._player_rack if players else self._bot_rack
        )
        for tile in tiles:
            if not tile.is_blank:
                new_rack.remove(tile)
                continue
            new_rack.remove(
                next(tile for tile in new_rack if tile.is_blank)
            )
        if players:
            self._player_rack = new_rack
        else:
            self._bot_rack = new_rack

    def get_move(self, players_turn: bool) -> Move:
        """
        Gets player's move from board or bot's move from 
        move finder.
        """
        if players_turn:
            return Move(self._board.get_placed_tiles())
        return self._move_finder.get_move(self._bot_rack)
    
    def process_move(self, move: Move) -> MoveResult:
        """Returns processing result from move processor."""
        return self._move_processor.process(move)

    def apply_move(
            self, move_result: MoveResult, players_turn: bool
        ) -> None:
        """
        Applies move to board object, restrict board, and 
        updates game state.
        """
        move = move_result.move
        formed_words = move_result.formed_words

        # Player's move will not yet have score
        if not move.score:
            move.score = self._move_processor.get_score(
            formed_words.main_word # type: ignore
        )
        
        # Apply move and restrict
        self._board.apply_move(move.placements)
        self._restrictor.restrict_board(formed_words)

        # Update game state
        self._turn += 1
        if players_turn:
            self._player_points += move.score
        else:
            self._bot_points += move.score
        

class MoveProcessor:
    """Applies move restictions to board for move searching."""

    def __init__(self, board: ScrabbleBoard, trie: Trie) -> None:
        self._board: ScrabbleBoard = board
        self._trie: Trie = trie
    
    def process(self, move: Move) -> MoveResult:
        """Derives and validate move, returning move result."""
        flags = ValidationFlags()
        formed_words = FormedWords()

        self._derive_and_validate(move, flags, formed_words)
        validation_result = self._validate_move(flags)

        return MoveResult(move, formed_words, validation_result)
    
    def _derive_and_validate(
            self, move: Move, flags: ValidationFlags, 
            formed_words: FormedWords
        ) -> None:
        """Derives and validates move coordinates and formed words."""
        # Determine if placements are horizontal or vertical
        # Assumes placement is horizontal (edge case in scorer)
        is_horizontal: bool = (
            len(set(tile.row for tile in move.placements)) == 1
        )

        # Validate coordinates of entry
        valid_coords: bool = self._validate_coordinates(
            move.placements, flags, is_horizontal
        )
        if not valid_coords:
            return
        
        # Derive and validate words formed by entry
        self._derive_formed_words(
            move.placements, is_horizontal, formed_words
        )
        self._validate_formed_words(
            move.placements, flags, formed_words
        )
        
    def _validate_coordinates(
            self, placements: list[TilePlacement], flags: ValidationFlags, 
            is_horizontal: bool
        ) -> bool:
        """Validates what can be determined by placement coords."""
        if not placements:
            return False
        flags.tiles_submitted = True
        
        if self._board.is_blank:
            if len(placements) == 1:
                return False
            flags.uses_multiple_tiles = True
            
            midpoint = BOARD_SIZE // 2
            if not any(
                (tile.row, tile.col) == (midpoint, midpoint) 
                for tile in placements
            ):
                return False
            flags.uses_center_square = True
        
        col_span = len(set(tile.col for tile in placements))
        if (not is_horizontal and col_span > 1):
           return False
        flags.forms_straight_line = True

        return True    

    def _derive_formed_words(
            self, placements: list[TilePlacement], is_horizontal: bool, 
            formed_words: FormedWords
        ) -> None:
        """Derives new words formed by move placements."""
        # Dict mapping coords to placements for quick lookup
        placement_lookup: dict[tuple[int, int], TilePlacement] = {
            (tile.row, tile.col): tile for tile in placements
        }

        # Get main word (horizontal word if horizontal & vice versa)
        tile: TilePlacement = placements[0]
        main_word = self._construct_word(
            tile, placement_lookup, is_horizontal=is_horizontal
        )
        formed_words.main_word = main_word

        # Derive cross words
        cross_words: list[FormedWord] = []
        for tile in placements:
            word = self._construct_word(
                tile, placement_lookup, 
                is_horizontal=not is_horizontal
            )
            cross_words.append(word)
        formed_words.cross_words = cross_words 

    def _construct_word(
            self, tile: TilePlacement, placement_lookup: dict, 
            is_horizontal: bool
        ) -> FormedWord:
        """Returns formed word for tiles in given board line."""
        placed_tiles: list[TilePlacement] = (
            self.get_word_tiles(tile.row, tile.col, 
                is_horizontal, placement_lookup) 
        )
        return FormedWord(
            tiles=placed_tiles, is_horizontal=is_horizontal
        )  

    def get_word_tiles(
            self, row: int, col: int, row_check: bool, 
            placement_lookup: dict | None = None
        ) -> list[TilePlacement]:
        """
        Returns tiles comprising word in given line and
        containing given index.
        """
        placed_tiles: list[TilePlacement] = []
        dr, dc = (0, 1) if row_check else (1, 0)

        # Loop backwards first to find first index
        while True:
            if row < 0 or col < 0:
                break
            if not (
                placement_lookup 
                and placement_lookup.get((row, col), None) 
                or self._board.board[row][col].tile
            ):
                break
            row -= dr
            col -= dc

        # Loop continued past last cell
        # Move forward by one cell
        row += dr
        col += dc

        # Loop forward to construct word
        while True:
            if row >= BOARD_SIZE or col >= BOARD_SIZE:
                break
        
            tile_placement = (
                placement_lookup.get((row, col), None) 
                if placement_lookup else None
            )  
            if not tile_placement:
                tile = self._board.board[row][col].tile
                tile_placement = (
                    TilePlacement(tile, row, col) if tile else None
                )
            if not tile_placement:
                break

            placed_tiles.append(tile_placement)
            row += dr
            col += dc

        return placed_tiles    

    def _validate_formed_words(
            self, placements: list[TilePlacement], flags: ValidationFlags,
            formed_words: FormedWords
        ) -> None:
        """
        Ensures words connect to pre-placed word (unles board was blank), 
        and that all words are real words.
        """
        # First word is not connected
        if self._board.is_blank:
            connected = True
            flags.is_connected = True
        else:
            connected = False

        main_word = formed_words.main_word
        if not main_word:
            return
        
        # Check main line for gaps
        if not self._has_no_gaps(main_word, placements):
            return
        flags.no_gaps = True
        
        for formed_word in (main_word, *formed_words.cross_words):
            if len(formed_word.tiles) == 1:
                # Not an actual word, don't check
                continue

            # Validate existence of word
            word: str = (
                "".join([tile.tile.letter 
                for tile in formed_word.tiles]) 
            )

            if not self._trie.word_exists(word):
                flags.invalid_word = word
                return

            if connected: continue # No need to check
            
            if self._is_connected(formed_word, placements):
                # Word is connected, set flag
                connected = True
                flags.is_connected = True 
    
    def _has_no_gaps(
            self, main_word: FormedWord, 
            placements: list[TilePlacement]
        ) -> bool:
        """Returns true if all placements appear in main line."""
        # Count number of tiles that were placed on current turn
        placed_tile_count = len(
            [tile for tile in main_word.tiles 
            if tile in placements]
        )
        # Placed tiles must include all entry tiles
        # If not, there must be gaps in the main line
        if len(placements) != placed_tile_count:
            return False
        return True

    def _is_connected(
            self, formed_word: FormedWord, 
            placements: list[TilePlacement]
        ) -> bool:
        """
        Returns true if a letter in word was not placed on 
        current move.
        """
        for tile in formed_word.tiles:
            if tile not in placements:
                return True
        return False
    
    def _validate_move(self, flags: ValidationFlags) -> ValidationResult:
        """Evaluates validation flags and returns a ValidationResult."""
        result = ValidationResult()

        if not flags.tiles_submitted:
            result.reason = "No tiles submitted"
        
        elif self._board.is_blank and not flags.uses_multiple_tiles:
            result.reason = "Use multiple tiles"
            
        elif self._board.is_blank and not flags.uses_center_square:
            result.reason = "Must use center square"
        
        elif not flags.forms_straight_line:
            result.reason = "Must form a straight line"
        
        elif not flags.no_gaps:
            result.reason = "Word cannot have gaps"
        
        elif flags.invalid_word:
            result.reason = f"Invalid word: {flags.invalid_word}"
        
        elif not flags.is_connected:
            result.reason = "Word must connect to an existing word"
        
        else:
            result.is_valid = True

        return result

    def get_score(self, main_word: FormedWord) -> int:
        """Returns the score of a move using main word."""
        score: int = 0
        tiles_used: int = 0
        main_word_points: int = 0
        main_word_mult: int = 1

        for tile in main_word.tiles:
            cross_points: int = 0
            cross_mult: int = 1

            cell: Cell = self._board.board[tile.row][tile.col]

            tile_pts: int = (
                LETTER_SCORES[JOKER_CHAR] if tile.tile.is_blank
                else LETTER_SCORES[tile.tile.letter] 
            )

            if cell.state == CellState.LOCKED:
                # Multipliers do not apply for locked tiles
                main_word_points += tile_pts
                continue
            
            tiles_used += 1
            cell_type: CellType = cell.type

            if cell_type == CellType.DOUBLE_LETTER:
                tile_pts *= 2
                
            elif cell_type == CellType.TRIPLE_LETTER:
                tile_pts *= 3
            
            elif cell_type == CellType.DOUBLE_WORD:
                cross_mult *= 2
                
            elif cell_type == CellType.TRIPLE_WORD:
                cross_mult *= 3

            restriction = (
                cell.row_restrictions if main_word.is_horizontal 
                else cell.col_restrictions
            )

            if restriction:
                cross_points = (
                    (tile_pts + restriction.cell_points) 
                    * cross_mult
                )
            
            main_word_points += tile_pts
            main_word_mult *= cross_mult
            score += cross_points
        
        if len(main_word.tiles) != 1:
            # Edge case due to horizontal assumption.
            # Cross word is ignored if main word is one tile
            score += main_word_points * main_word_mult

        if tiles_used == RACK_SLOTS:
            # Using entire rack results is a bingo
            score += BINGO_BONUS

        return score


class BoardRestrictor:
    """Applies restrictions to cells in board for move search."""

    def __init__(
            self, board: ScrabbleBoard, trie: Trie, 
            move_processor: MoveProcessor
        ) -> None:
        self._board: ScrabbleBoard = board
        self._trie: Trie = trie
        self._move_processor: MoveProcessor = move_processor
    
    def restrict_board(self, formed_words: FormedWords) -> None:
        """Determines and restricts anchors created by move."""
        anchors: list[AnchorCell] = self._retrieve_anchors(formed_words)
        self._restrict_anchors(anchors)
    
    def _retrieve_anchors(self, formed_words: FormedWords) -> list[AnchorCell]:
        """Returns list of anchor cells created by move."""
        anchors: list[AnchorCell] = []
        
        for word in (formed_words.main_word, *formed_words.cross_words):
            if not word: continue # For type checker

            row, col = word.tiles[0].row, word.tiles[0].col
            dr, dc = (0, 1) if word.is_horizontal else (1, 0)

            # Get cell before beginning of word
            before_row, before_col = row - dr, col - dc
           
            if before_row >= 0 and before_col >= 0:
                # Cell exists before word
                before_anchor = self._get_before_anchor(
                    word, before_row, before_col, 
                    is_horizontal=word.is_horizontal
                )
                anchors.append(before_anchor)
            
            # Get cell after end of word
            length = len(word.tiles)
            after_row, after_col = (
                row + (dr * length), col + (dc * length)
            )

            if after_row < BOARD_SIZE and after_col < BOARD_SIZE:
                # Cell exists after word
                after_anchor = self._get_after_anchor(
                    word, after_row, after_col, 
                    is_horizontal=word.is_horizontal
                )
                anchors.append(after_anchor)
        return anchors

    def _get_before_anchor(
            self, word: FormedWord, anchor_row: int, anchor_col: int, 
            is_horizontal: bool
        ) -> AnchorCell:
        """Returns anchor cell before given word.""" 
        dr, dc = (0, 1) if word.is_horizontal else (1, 0)

        # Get cell before anchor, 2 before start of word
        prefix_row, prefix_col = anchor_row - dr, anchor_col - dc

        if prefix_row < 0 or prefix_col < 0:
            # No cell preceeding anchor, therefore no prefix
            prefix = []
        else:
            prefix = self._move_processor.get_word_tiles(
                row=prefix_row, col=prefix_col, row_check=is_horizontal
            )
        return AnchorCell(
            row=anchor_row, col=anchor_col, prefix=prefix, 
            suffix=word.tiles, is_horizontal=word.is_horizontal
        )
    
    def _get_after_anchor(
            self, word: FormedWord, anchor_row: int, anchor_col: int, 
            is_horizontal: bool
        ) -> AnchorCell:
        """Returns anchor cell after given word."""
        # Edge case: get_word_tiles will move forward after seeing 
        # blank tile. Therefore input after cell to get correct suffix
        suffix = self._move_processor.get_word_tiles(
                row=anchor_row, col=anchor_col, row_check=is_horizontal
            )

        return AnchorCell(
            row=anchor_row, col=anchor_col, prefix=word.tiles, 
            suffix=suffix, is_horizontal=word.is_horizontal
        )
    
    def _restrict_anchors(self, anchors: list[AnchorCell]) -> None:
        """
        Determines letter restrictions for anchor and calculates 
        points gained by placing in anchor for quick scoring.
        """
        for anchor in anchors:
            cell = self._board.board[anchor.row][anchor.col]

            # Use morpheme strings to find restrictions
            str_prefix: str = (
                "".join([tile.tile.letter for tile in anchor.prefix]) 
            )
            str_suffix: str = (
                "".join([tile.tile.letter for tile in anchor.suffix]) 
            )
            restrictions: list[str] = (
                self._trie.between_letters(str_prefix, str_suffix)     
            )

            # Get points of tiles in morphemes for later scoring 
            prefix_points: int = (
                sum([tile.tile.points for tile in anchor.prefix]) 
            )
            suffix_points: int = (
                sum([tile.tile.points for tile in anchor.suffix]) 
            )

            cell_restriction = CellRestriction(
                restrictions, suffix_points + prefix_points
            )
            
            # Restrict corresponding attribute in cell
            if anchor.is_horizontal:
                cell.col_restrictions = cell_restriction
            else:
                cell.row_restrictions = cell_restriction