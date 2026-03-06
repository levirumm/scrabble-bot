from app.gui.view import ScrabbleView
from app.model.model import ScrabbleModel
from app.model.types import (
    Tile, FormedWord, Move, MoveResult, ValidationResult
)
from app.model.constants import RACK_SLOTS


class ScrabbleController:
    """
    Controller of application which handles events and 
    coordinates updates of model and view.
    """
    def __init__(
            self, view: ScrabbleView, model: ScrabbleModel
        ) -> None:
        self._view: ScrabbleView = view
        self._model: ScrabbleModel = model

        self._start_game()

        # Connect slots to button panel
        self._view.game_area.skipPressed.connect(self._on_skip)
        self._view.game_area.swapPressed.connect(self._on_swap)
        self._view.game_area.submitPressed.connect(self._on_submit)

        # Connect slots to game events
        self._view.game_area.tilePlaced.connect(
            self._on_tile_placed
        )
        self._view.game_area.tileRemoved.connect(
            self._on_tile_removed
        )

        # Connect slots to button console
        self._view.button_console.infoPressed.connect(
            self._view.open_game_info
        )
        self._view.button_console.dictPressed.connect(
            self._view.open_dictionary
        )
        self._view.button_console.peekPressed.connect(
            self._see_bot_rack
        )
        self._view.button_console.hintPressed.connect(
            self._get_hint
        )

    def _on_submit(self) -> None:
        self._turn(players=True)
    
    def _on_tile_placed(
            self, row: int, col: int, tile: Tile
        ) -> None:
        """Adds tile placement to model."""
        self._model.board.place_tile(row, col, tile)
    
    def _on_tile_removed(self, row: int, col: int) -> None:
        """Removes tile placement from model."""
        self._model.board.remove_tile(row, col)
    
    def _see_bot_rack(self) -> None:
        """Opens menu showing bot's tiles to user."""
        bot_tiles = self._model.bot_rack
        self._view.open_bot_peek(bot_tiles)
    
    def _get_hint(self) -> None:
        """
        Gets a hint from move finder, previews, and applies 
        if user accepts.
        """
        self._view.game_area.recall()

        # Get move from move finder
        move = self._model.get_move(players=True)
        if not move.placements:
            print("No move found")
            return

        self._view.game_area.show_hint_preview(move.placements)

        # Ask user if they will accept hint
        if not self._view.open_hint_menu():
            self._view.game_area.remove_hint_preview()
            return
        self._view.game_area.remove_hint_preview()

        # Update any pending tiles from bot move
        self._view.game_area.update_pending()

        # Process and apply move
        result = self._model.process_move(move)
        self._model.apply_move(result, players=True)
        self._update_game(move, result, players=True, hint=True)
        self._view.game_area.apply_move(move.placements)

        # Tiles should not be pending
        self._view.game_area.update_pending()

        self._turn(players=False)

    def _on_swap(self) -> None:
        """
        Allows user to select tiles to swap. Gets new tiles 
        from letter bag and skips players turn.
        """
        if self._model.remaining_tiles < RACK_SLOTS:
            # Cannot skip if less than 7 tiles
            print(
                "Cannot swap with less than " \
                "7 tiles remaining."
            )
            return
        
        self._view.game_area.recall()

        # Open tile swap menu
        selected = self._view.open_tile_swap(
            self._model.player_rack
        )
        if not selected: return
        
        # Get new tiles from model and update rack
        new_tiles = self._model.select_tiles(len(selected))
        self._model.update_rack(
            players=True, used_tiles=selected, 
            new_tiles=new_tiles
        )
        self._view.game_area.update_player_rack(
            new_tiles=new_tiles, used_tiles=selected, 
            racked=True
        )
        self._on_skip() # Skip players turn
    
    def _on_skip(self) -> None:
        """
        Recalls tiles, skips player's turn, and initiates 
        bot's turn.
        """
        self._view.game_area.recall()
        self._model.skip()
        self._view.game_area.update_pending()

        self._view.update_turn_history(
            self._model.turn, players=True
        )
        self._turn(players=False)
    
    def _turn(self, players: bool) -> None:
        """Gets move, processes and applies if valid."""
        move = (
            self._model.get_player_move() if players 
            else self._model.get_move(players=False)
        )

        if not players and not move.placements:
            # Bot was unable to find move. Skip turn.
            self._model.skip()
            self._view.update_turn_history(
                self._model.turn, players
            )
            print("Scrabble bot skipped")
            return

        result = self._model.process_move(move)
        if not self._validate_move(result.validation_result):
            return

        self._model.apply_move(result, players=players)

        self._update_game(move, result, players)

        if players:
            # Initiate bot's turn
            self._turn(players=False)
    
    def _validate_move(
            self, validation_result: ValidationResult
        ) -> bool:
        """Returns true if move is valid."""
        if not validation_result.is_valid:
            print(validation_result.reason)
            return False
        return True

    def _update_game(
            self, move: Move, result: MoveResult, 
            players: bool, hint: bool = False
        ) -> None:
        """Applies move to model and updates GUI."""
        # Get new tiles
        new_tiles = self._model.select_tiles(
            len(result.move.placements)
        )
        used_tiles = [tp.tile for tp in result.move.placements]

        # Update letter rack of move maker
        self._model.update_rack(
            players, new_tiles, used_tiles
        )

        # Update info panel and turn history
        game_state = self._model.game_state
        self._view.update_info_panel(game_state)

        # Apply move to turn history
        formed_str = self._formed_words_to_strings(
            [result.formed_words.main_word] 
            + result.formed_words.cross_words
        )
        self._view.update_turn_history(
            game_state.turn, players, 
            move.score, formed_str
        )

        # Update rack if players, else update board
        if players:
            self._view.game_area.update_player_rack(
                new_tiles, used_tiles, hint=hint
            )
        else:
            self._view.game_area.apply_move(
                result.move.placements
            )

    def _start_game(self) -> None:
        """Set initial conditions of Scrabble game."""
        # Initiate full letter racks for player and bot
        player_tiles = self._model.select_tiles(RACK_SLOTS)
        bot_tiles = self._model.select_tiles(RACK_SLOTS)

        self._model.update_rack(players=True, new_tiles=player_tiles)
        self._model.update_rack(players=False, new_tiles=bot_tiles)

        # Update letter rack widget
        self._view.game_area.update_player_rack(player_tiles)

        # Update info panel to match model
        self._view.update_info_panel(self._model.game_state)

    def _formed_words_to_strings(
            self, formed_words: list[FormedWord | None]
        ) -> list[str]:
        """
        Helper function which converts formed words to strings.
        """
        formed_str = [] # Formed word strings for history
        for word in formed_words:
            if len(word.tiles) == 1: # type: ignore
                continue
            formed_str.append(
                "".join(tile.tile.letter 
                for tile in word.tiles) # type: ignore
            )
        return formed_str