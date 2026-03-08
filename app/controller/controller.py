from PySide6.QtCore import QTimer
from app.gui.view import ScrabbleView
from app.model.model import ScrabbleModel
from app.model.types import (
    Tile, FormedWord, Move, MoveResult, 
    ValidationResult, ToastType
)
from app.model.constants import (
    RACK_SLOTS, MAX_CONSECUTIVE_SKIPS
)


class ScrabbleController:
    """
    Controller of application which handles events and 
    coordinates updates of model and view.
    """
    BOT_MOVE_DELAY: int = 2000

    def __init__(
            self, view: ScrabbleView, model: ScrabbleModel
        ) -> None:
        self._view: ScrabbleView = view
        self._model: ScrabbleModel = model

        self._view.connect_to_controller(self)

        self._start_game()

    def _on_submit(self) -> None:
        self._turn(players=True)
    
    def _on_tile_placed(
            self, row: int, col: int, tile: Tile
        ) -> None:
        self._model.board.place_tile(row, col, tile)
    
    def _on_tile_removed(self, row: int, col: int) -> None:
        self._model.board.remove_tile(row, col)
    
    def _see_bot_rack(self) -> None:
        bot_tiles = self._model.bot_rack
        self._view.open_bot_peek(bot_tiles)
    
    def _bot_move_after_delay(self) -> None:
        """
        Initiates not move after delay, disabling buttons 
        to prevent interference.
        """
        self._view.disable_for_bot_move(True)
        QTimer.singleShot(
            self.BOT_MOVE_DELAY, self._init_bot_move
        )
    
    def _init_bot_move(self) -> None:
        """Helper function called after delay."""
        self._view.disable_for_bot_move(False)
        self._turn(players=False)

    def _get_hint(self) -> None:
        """
        Gets a hint from move finder, previews, and applies 
        if user accepts.
        """
        self._view.game_area.recall()

        # Get move from move finder
        move = self._model.get_move(players=True)
        if not move.placements:
            self._view.show_toast(
                message="No move found", 
                toast_type=ToastType.INFO
            )
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
        self._update_rack(result, player=True, hint=True)
        self._update_game(move, result, players=True)
        self._view.game_area.apply_move(move.placements)

        # Tiles should not be pending
        self._view.game_area.update_pending()

        self._view.show_toast(
            message=f"{move.score} points", 
            toast_type=ToastType.PLAYER
        )

        self._bot_move_after_delay()

    def _on_swap(self) -> None:
        """
        Allows user to select tiles to swap. Gets new tiles 
        from letter bag and skips players turn.
        """
        if self._model.remaining_tiles < RACK_SLOTS:
            # Cannot skip if less than 7 tiles
            self._view.show_toast(
                message=(
                    "Cannot swap with less "
                    "than 7 tiles remaining"
                ), 
                toast_type=ToastType.INFO
            )
            return

        # Open tile swap menu
        selected = self._view.open_tile_swap(
            self._model.player_rack
        )
        if not selected: return

        self._view.game_area.recall()
        
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
        """Recalls tiles and skips turn."""
        self._view.game_area.recall()
        self._skip(player=True)
    
    def _skip(self, player: bool) -> None:
        """Skips turn and inititates opponent turn."""
        self._model.skip()
        self._view.game_area.update_pending()
        self._view.update_turn_history(
            self._model.turn, players=player
        )
        self._consective_skips += 1

        if self._consective_skips >= MAX_CONSECUTIVE_SKIPS:
            print("game_over")
            return
        
        if player:
            self._turn(players=not player)

    def _turn(self, players: bool) -> None:
        """Gets move, processes and applies if valid."""
        move = (
            self._model.get_player_move() if players 
            else self._model.get_move(players=False)
        )

        if not players and not move.placements:
            # Bot was unable to find move. Skip turn.
            self._view.show_toast(
                message="Scrabble Bot skipped", 
                toast_type=ToastType.BOT
            )
            self._skip(player=False)
            return

        result = self._model.process_move(move)
        if not self._validate_move(result.validation_result):
            return
        
        self._consective_skips = 0

        self._model.apply_move(result, players=players)

        self._update_rack(result, players)

        self._update_game(move, result, players)

        toast_type = (
            ToastType.PLAYER if players else ToastType.BOT
        )
        self._view.show_toast(
            message=f"{move.score} points", 
            toast_type=toast_type
        )

        if players:
           self._bot_move_after_delay()

    def _validate_move(
            self, validation_result: ValidationResult
        ) -> bool:
        """Returns true if move is valid."""
        if not validation_result.is_valid:
            self._view.show_toast(
                message=validation_result.reason, 
                toast_type=ToastType.ERROR
            )
            return False
        return True
    
    def _update_rack(
            self, result: MoveResult, player: bool, 
            hint: bool = False
        ) -> None:
        new_tiles = self._model.select_tiles(
            len(result.move.placements)
        )
        used_tiles = [tp.tile for tp in result.move.placements]

        # Update letter rack of move maker
        self._model.update_rack(
            player, new_tiles, used_tiles
        )

        if player:
            self._view.game_area.update_player_rack(
            new_tiles, used_tiles, hint=hint
        )

    def _update_game(
            self, move: Move, result: MoveResult, 
            players: bool
        ) -> None:
        """Applies move to model and updates GUI."""
        # Update info panel and turn history
        game_state = self._model.game_state
        self._view.update_info_panel(game_state)

        # Apply move to turn history
        formed_str = self._model.formed_words_to_strings(
            [result.formed_words.main_word] 
            + result.formed_words.cross_words
        )
        self._view.update_turn_history(
            game_state.turn, players, 
            move.score, formed_str
        )

        # Update rack if players, else update board
        if not players:
            self._view.game_area.apply_move(
                result.move.placements
            )

    def _start_game(self) -> None:
        """Set initial conditions of Scrabble game."""
        self._consective_skips: int = 0
        
        # Initiate full letter racks for player and bot
        player_tiles = self._model.select_tiles(RACK_SLOTS)
        bot_tiles = self._model.select_tiles(RACK_SLOTS)

        self._model.update_rack(players=True, new_tiles=player_tiles)
        self._model.update_rack(players=False, new_tiles=bot_tiles)

        # Update letter rack widget
        self._view.game_area.update_player_rack(player_tiles)

        # Update info panel to match model
        self._view.update_info_panel(self._model.game_state)