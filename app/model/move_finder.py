from app.model.types import (
    Cell, CellState, Tile, CellRestriction, 
    TrieNode, TilePlacement, Move, FormedWord
)
from app.model.game_objects import ScrabbleBoard
from app.model.constants import (
    BOARD_SIZE, RACK_SLOTS, JOKER_CHAR
)
from app.model.trie import Trie


class MoveFinder:
    """
    Finds highest scoring moves given board and letter 
    rack.
    """
    def __init__(
            self, board: ScrabbleBoard, trie: Trie, 
            move_processor: "MoveProcessor" # type: ignore
        ) -> None:
        self._board: ScrabbleBoard = board
        self._move_processor = move_processor
        self._trie: Trie = trie
    
    def get_move(self, rack: list[Tile]) -> Move:
        """Finds and returns highest scoring move."""
        best_score: int = 0
        best_word: FormedWord | None = None

        # Get highest scoring bot move
        possible: list[FormedWord] = (
            self._get_possible_words(rack)
        )
        for word in possible:
            score = self._move_processor.get_score(word)
            if score > best_score:
                best_score = score
                best_word = word
        if not best_word:
            placed_tiles = []
        else:
            # Determine bot tiles comprising word
            placed_tiles = [
                tile for tile in best_word.tiles
                if self._board.board[tile.row][tile.col].state 
                != CellState.LOCKED
            ]
        return Move(placed_tiles, best_score)

    def _get_possible_words(self, rack: list[Tile]) -> list[FormedWord]:
        """Returns all possible words Scrabble bot can make."""
        if self._board.is_blank:
            # Lazy approach: Start word from center cell
            # Does not return necessarily highest scoring move
            center: int = BOARD_SIZE // 2
            line = self._board.board[center]
            return (
                self._get_index_words(
                    rack, line, center, row=True
                )
            )

        placements: list[FormedWord] = []

        # Check all rows for possible placements
        for row in self._board.board:
            placements.extend(
                self._get_line_words(rack, row, is_row=True)
            )
        
        # Check all columns for possible placements
        for c in range(BOARD_SIZE):
            col = [self._board.board[i][c] for i in range(BOARD_SIZE)]
            placements.extend(
                self._get_line_words(rack, col, is_row=False)
            )
        
        return placements
    
    def _get_line_words(
            self, rack: list[Tile], line: list[Cell], 
            is_row: bool
        ) -> list[FormedWord]:
        """
        Returns all possible words that can be made in line.
        """
        placements: list[FormedWord] = []

        # Get indices of possible starting cells
        # Return if none
        starting_indices = (
            self._get_starting_indices(line, is_row)
        )
        if not starting_indices:
            return placements

        # Get possible words from each index
        for index in starting_indices:
            placements.extend(
                self._get_index_words(rack, line, index, is_row)
            )
        return placements
                
    def _get_starting_indices(
            self, line: list[Cell], row: bool
        ) -> list[int]:
        """
        Returns indices of cells from which a new word could 
        start.
        """
        starting_indices: list[int] = []
        reach: int = 0

        # Iterate backwards through line
        for i in range(len(line) - 1, -1, -1):
            if i == BOARD_SIZE - 1:
                continue

            cell = line[i]

            if i != 0:
                behind_cell = line[i - 1]
                if behind_cell.tile:
                    continue 

            if cell.tile:
                # Can place entire rack before locked tile
                reach = RACK_SLOTS 
                starting_indices.insert(0, i)
                continue
            
            restriction: CellRestriction | None = (
                cell.row_restrictions 
                if row else cell.col_restrictions
            )

            if restriction:
                # Cell is an anchor
                # Can place one less than rack before anchor
                starting_indices.insert(0, i)
                reach = RACK_SLOTS - 1 
                continue
                
            if reach > 0:
                # Word can reach locked tile or anchor from here
                # Record index and decrease reach
                starting_indices.insert(0, i)
                reach -= 1

        return starting_indices

    def _get_index_words(
            self, rack: list[Tile], line: list[Cell], 
            idx: int, row: bool
        ) -> list[FormedWord]:
        """
        Returns all words that can be made starting on given 
        index.
        """
        search = RecursiveSearch(
            root=self._trie.root, rack=rack, line=line, 
            idx=idx, is_row=row, is_blank=self._board.is_blank, 
            trie=self._trie
        )
        return search.get_all()


class RecursiveSearch:
    """
    Uses recursive algorithm to search all word placements 
    in a board line from a given index.
    """
    def __init__(
            self, root: TrieNode, rack: list[Tile], 
            line: list[Cell], idx: int, is_row: bool, 
            is_blank: bool, trie: Trie
        ) -> None:
        self._line: list[Cell] = line
        self._is_row: bool = is_row
        self._possible_words: list[FormedWord] = []
        self._trie = trie

        self.search(
            node=root, path=[], rack=rack, idx=idx, 
            connected=is_blank
        )

    def get_all(self) -> list[FormedWord]:
        return self._possible_words

    def search(
            self, node: TrieNode, rack: list[Tile], idx: int, 
            path: list[TilePlacement], tiles_used: int = 0, 
            connected: bool = False
        ) -> None:
        """
        Recursiverly searches all paths of trie which can form 
        valid words.
        """
        if idx >= BOARD_SIZE:
            # Progressed past last cell
            # Check for valid word and return
            if (connected and node.end and tiles_used > 0):
                self._possible_words.append(
                    FormedWord(path, is_horizontal=self._is_row)
                )
            return
        
        cell = self._line[idx]
        
        if cell.tile:
            char = cell.tile.letter
            if char not in node.children:
                # Path cannot contain tile
                return
            
            t = TilePlacement(cell.tile, cell.row, cell.col)

            self.search(
                node.children[char], rack, idx + 1, path + [t], 
                tiles_used, connected=True
            )
            return # Checked all paths from this cell

        # Cell does not contain tile. Check path leading to cell.
        if (connected and node.end and tiles_used > 0):
            self._possible_words.append(
                FormedWord(path, is_horizontal=self._is_row)
            )
        
        # Check cell for restriction
        restriction: CellRestriction | None = (
                cell.row_restrictions if self._is_row 
                else cell.col_restrictions
            )
        
        if restriction and not restriction.restrictions:
            # No possible tile can meet restrictions
            # Do not search
            return
        
        # If there is a restriction, uses anchor and is connected
        now_connected = connected or bool(restriction)
        
        # Get set of possible letters that can be placed in position
        letter_options: set[str] = set()
        for tile in rack:
            if tile.is_blank:
                letter_options.add(JOKER_CHAR)
            elif (
                (not restriction) or 
                (restriction and tile.letter in restriction.restrictions)
            ):
                letter_options.add(tile.letter)
    
        for letter in letter_options:
            # Get corresponding tile
            if letter == JOKER_CHAR:
                tile = next(
                    (tile for tile in rack if tile.is_blank), None
                )
            else:
                tile = next(
                    (tile for tile in rack if tile.letter == letter), None
                )
            
            if tile is None:
                continue  # Skip this letter option safely

            if tile.is_blank:
                path_options = node.children.keys()

                # Options for cell must meet path options and restrictions
                options: set[str] = set(
                    path_options & restriction.restrictions 
                    if restriction else path_options
                )

                # Try all possible options for cell
                for char in options:
                    new_tile = Tile(char, 0, is_blank=True)
                    new_rack = rack.copy()
                    new_rack.remove(tile)

                    t = TilePlacement(new_tile, cell.row, cell.col)

                    self.search(
                        node.children[char], new_rack, idx + 1, 
                        path + [t], tiles_used + 1, connected=now_connected
                    )
                continue
            
            if letter not in node.children:
                # Valid word cannot be formed using letter
                continue
            
            # Try tile in position
            new_rack = rack.copy()
            new_rack.remove(tile)

            t = TilePlacement(tile, cell.row, cell.col)

            self.search(
                node.children[letter], new_rack, idx + 1, 
                path + [t], tiles_used + 1, connected=now_connected
            )