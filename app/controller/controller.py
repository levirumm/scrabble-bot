from PySide6.QtCore import QTimer
from app.gui.view import ScrabbleView
from app.model.model import ScrabbleModel
from app.model.types import (
    Tile, Move, MoveResult, ToastType, 
    TurnType
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

    def _on_tile_placed(
            self, row: int, col: int, tile: Tile
        ) -> None:
        self._model.board.place_tile(row, col, tile)
    
    def _on_tile_removed(self, row: int, col: int) -> None:
        self._model.board.remove_tile(row, col)
    
    def _see_bot_rack(self) -> None:
        bot_tiles = self._model.bot_rack
        self._view.open_bot_peek(bot_tiles)
    
    def _on_resign(self) -> None:
        if self._view.open_resign_dialog():
            self._on_game_over(resigned=True)

    def _player_turn(self) -> None:
        self._move(TurnType.PLAYER)

    def _get_hint(self) -> None:
        self._view.game_area.recall()
        self._move(TurnType.HINT)
    
    def _bot_turn_after_delay(self) -> None:
        """
        Initiates not move after delay, disabling buttons 
        to prevent interference.
        """
        self._view.disable_for_bot_move(True)
        QTimer.singleShot(
            self.BOT_MOVE_DELAY, self._init_bot_turn
        )
    
    def _init_bot_turn(self) -> None:
        """Helper function called after delay."""
        self._view.disable_for_bot_move(False)
        self._move(TurnType.BOT)
    
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
            self._on_game_over()
            return
        
        if player:
            self._move(TurnType.BOT)
    
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
    
    def _move(self, turn_type: TurnType) -> None:
        """Initiates a player, bot, or hint turn."""
        move = self._get_move(turn_type)

        if not self._handle_no_move(turn_type, move):
            return
        
        if (
            turn_type is TurnType.HINT and 
            not self._ask_accept_hint(move)
        ):
            # Return if hint is not accepted
            return

        result = self._model.process_move(move)

        # Check validation flags for player move
        if (
            turn_type is TurnType.PLAYER and 
            not result.validation_result.is_valid
        ):
            self._view.show_toast(
                message=result.validation_result.reason, 
                toast_type=ToastType.ERROR
            )
            return

        new_tiles = self._apply_move(move, result, turn_type)
        
        player = turn_type is not TurnType.BOT

        self._show_move_toast(move, player)

        if self._is_terminating_move(new_tiles, player):
            self._on_game_over()
            return
    
        if turn_type is not TurnType.BOT:
            self._bot_turn_after_delay()
    
    def _get_move(self, turn_type: TurnType):
        """Gets the move for each turn type."""
        if turn_type is TurnType.PLAYER:
            return self._model.get_player_move()
        return self._model.get_move(turn_type is TurnType.HINT)

    def _handle_no_move(
            self, turn_type: TurnType, move: Move
        ) -> bool:
        """Handles no move cases for each turn type."""
        if move.placements:
            return True

        if turn_type is TurnType.HINT:
            self._view.show_toast("No move found", ToastType.INFO)
            return False

        if turn_type is TurnType.BOT:
            self._view.show_toast("Scrabble Bot skipped", ToastType.BOT)
            self._skip(player=False)
            return False
        return True
    
    def _apply_move(
            self, move: Move, result: MoveResult, 
            turn_type: TurnType
        ) -> list[Tile]:
        """
        Applies move to model and updates view elements based 
        on move type.
        """
        # Update model
        player = turn_type is not TurnType.BOT
        self._consective_skips = 0
        self._model.apply_move(result, players=player)
        new_tiles, used_tiles = self._update_model_rack(
            result, player=player
        )

        # Update info panel
        self._update_info_panel(move, result, players=player)

        # Update view elements for move type
        if turn_type is TurnType.PLAYER:
            self._view.game_area.update_player_rack(new_tiles, used_tiles)

        elif turn_type is TurnType.BOT:
            self._view.game_area.apply_move_to_board(move.placements)

        elif turn_type is TurnType.HINT:
            self._view.game_area.update_player_rack(
                new_tiles, used_tiles, hint=True
            )
            self._view.game_area.apply_move_to_board(
                move.placements, pending=False
            )
        return new_tiles
        
    def _ask_accept_hint(self, move: Move) -> bool:
        """
        Opens menu to ask user to accep hint, returning true 
        if user accepts.
        """
        self._view.game_area.show_hint_preview(move.placements)
        if not self._view.open_hint_menu():
            self._view.game_area.remove_hint_preview()
            return False
        self._view.game_area.remove_hint_preview()

        # Update any pending tiles from bot move
        self._view.game_area.update_pending()
        return True

    def _is_terminating_move(
            self, new_tiles: list[Tile], player: bool
        ) -> bool:
        """Returns true if no tiles and mover's rack is empty."""
        return (
            not new_tiles and 
            self._model.empty_rack(player=player)
        )
        
    def _show_move_toast(self, move: Move, player: bool) -> None:
        """Shows toast for move."""
        self._view.show_toast(
            message=f"{move.score} points", 
            toast_type=(
                ToastType.PLAYER if player 
                else ToastType.BOT
            )
        )
    
    def _update_model_rack(
            self, result: MoveResult, player: bool
        ) -> tuple:
        """
        Gets new tiles from letter bag and updates model 
        letter rack.
        """
        new_tiles = self._model.select_tiles(
            len(result.move.placements)
        )
        used_tiles = (
            [tp.tile for tp in result.move.placements]
        )
        self._model.update_rack(
            player, new_tiles, used_tiles
        )
        return new_tiles, used_tiles

    def _update_info_panel(
            self, move: Move, result: MoveResult, 
            players: bool
        ) -> None:
        """Applies move to info panel"""
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
    
    def _on_game_over(self, resigned: bool = False) -> None:
        """Opens the menu at the end of the game."""
        game_data = self._model.get_game_results(resigned)
        game_state = self._model.game_state
        self._view.update_info_panel(game_state)
        self._view.open_game_over_menu(game_data, resigned)
        self._model.reset()
        self._view.reset()
        self._start_game()
        
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