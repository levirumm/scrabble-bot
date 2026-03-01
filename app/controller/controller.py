from app.gui.view import ScrabbleView
from app.model.model import ScrabbleModel
from app.model.types import Tile, FormedWord
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

        # Initiate full letter racks for player and bot
        player_tiles = self._model.select_tiles(RACK_SLOTS)
        bot_tiles = self._model.select_tiles(RACK_SLOTS)
        self._view.update_player_rack(player_tiles)
        self._model.update_bot_rack(bot_tiles)

        # Update info panel to match model
        self._view.update_info_panel(self._model.game_state)

        # Connect slots to button panel
        self._view.game_area.submitPressed.connect(self._on_submit)
        self._view.game_area.skipPressed.connect(self._on_skip)

        # Connect slots to game events
        self._view.game_area.tilePlaced.connect(
            self._on_tile_placed
        )
        self._view.game_area.tileRemoved.connect(
            self._on_tile_removed
        )
    
    def _on_submit(self) -> None:
        self._turn(players_turn=True)
    
    def _on_skip(self) -> None:
        self._view.game_area.recall()
        self._model.skip()
        self._view.update_turn_history(
            self._model.turn, players=True
        )
        self._turn(players_turn=False)
        
    def _on_tile_placed(self, row: int, col: int, tile: Tile) -> None:
        self._model.board.place_tile(row, col, tile)
    
    def _on_tile_removed(self, row: int, col: int) -> None:
        self._model.board.remove_tile(row, col)

    def _turn(self, players_turn: bool) -> None:
        """Gets move from board, processes and applies if valid."""
        # Retrieve and process input
        move = self._model.get_move(players_turn)
        result = self._model.process_move(move)

        if not players_turn and not result.move.placements:
            # Skip bot's turn when unable to find move
            self._model.skip()
            self._view.update_turn_history(
                self._model.turn, players_turn
            )
            print("Scrabble bot skipped")
            return

        # Check if input is valid
        validation_result = result.validation_result
        if not validation_result.is_valid:
            print(validation_result.reason)
            return

        # Apply move to model and get new tiles
        self._model.apply_move(result, players_turn)
        new_tiles = self._model.select_tiles(
            len(result.move.placements)
        )
        used_tiles = result.move.placements

        # Update info panel and turn histroy
        game_state = self._model.game_state
        self._view.update_info_panel(game_state)

        # Apply move to turn history
        formed_str = self._formed_words_to_strings(
            [result.formed_words.main_word] 
            + result.formed_words.cross_words
        )
        self._view.update_turn_history(
            game_state.turn, players_turn, 
            move.score, formed_str
        )

        if players_turn:
            self._view.update_player_rack(new_tiles, used_tiles)
            # Initiate bot's turn
            self._turn(players_turn=False)
        else:
            self._view.apply_bot_move(result.move.placements)
            self._model.update_bot_rack(new_tiles, used_tiles)
    
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