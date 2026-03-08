from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import QObject, QPoint
from app.gui.layout.ui_scrabble_view import Ui_ScrabbleView
from app.model.types import (
    CellType, GameState, Tile, ToastType
)
from app.gui.palette.palette import PALETTE
from app.gui.button_console import ButtonConsole
from app.gui.game_area import GameArea
from app.gui.information_panel import InfoPanel
from app.gui.pop_ups import (
    TileSwap, LetterSelect, BotPeek, Dictionary,
    HintMenu, GameInfo, ToastManager
)
from pathlib import Path


class ScrabbleView(QWidget, Ui_ScrabbleView):
    """
    View of Scrabble Bot which handles UI elements, 
    styling, pop ups, and layout.
    """
    STYLE_PATHS: list[Path] = [
        Path(__file__).parent / "styles" / "central.qss",
        Path(__file__).parent / "styles" / "game_area.qss",
        Path(__file__).parent / "styles" / "info_panel.qss",
        Path(__file__).parent / "styles" / "button_console.qss",
        Path(__file__).parent / "styles" / "pop_ups.qss"
    ]

    def __init__(self, cell_types: list[list[CellType]]) -> None:
        super().__init__()
        self._ui = Ui_ScrabbleView()
        self._ui.setupUi(self)
        self.setWindowTitle("Scrabble Bot")

        # Initiate view wide styling
        self.setStyleSheet(self._load_qss()) 
        self.setProperty("role", "bg")

        # Create app widgets
        self._button_console = ButtonConsole(self._ui)
        self._game_area = GameArea(cell_types, self._ui)
        self._info_panel = InfoPanel(self._ui)

        self._game_area.letterRequired.connect(
            self.open_letter_select
        )

        self._toast_manager = ToastManager()

        # Open window in full screen
        self.showMaximized()
    
    @property
    def game_area(self) -> GameArea:
        return self._game_area

    @property
    def button_console(self) -> ButtonConsole:
        return self._button_console
    
    def show_toast(
            self, message: str, toast_type: ToastType
        ) -> None:
        """Creates a toast to display message."""
        self._toast_manager.show_toast(
            parent=self._ui.board_container, 
            message=message, type=toast_type
        )

    def open_game_info(self) -> None:
        """Opens game info menu."""
        game_info = GameInfo(self)
        game_info.exec()

    def open_dictionary(self) -> None:
        """Opens dictionary menu letting user search words."""
        dictionary = Dictionary(self)
        dictionary.exec()

    def open_bot_peek(self, bot_tiles: list[Tile]) -> None:
        """Opens menu letting user see bot's tiles."""
        bot_peek = BotPeek(self, bot_tiles)
        bot_peek.exec()
    
    def open_hint_menu(self) -> bool:
        """Opens dialog to choose to play suggested move."""
        hint_menu = HintMenu(self)
        pos = self._button_console.hint_button_coords()
        hint_menu.move(pos.x(), pos.y())

        result = hint_menu.exec()

        return result == QDialog.DialogCode.Accepted

    def open_tile_swap(self, tiles: list[Tile]) -> list[Tile] | None:
        """Opens tile swap menu and returns selected tiles.."""
        tile_swap = TileSwap(self, tiles)
        result = tile_swap.exec()

        if result == QDialog.DialogCode.Accepted:
            return tile_swap.selected
        return None

    def open_letter_select(self, tile: QObject) -> None:
        """Opens letter select menu for setting joker tile."""
        letter_select = LetterSelect(self)
        result = letter_select.exec()

        if result == QDialog.DialogCode.Accepted:
            selection = letter_select.selected_letter

        tile.update_letter(selection) # type: ignore
    
    def update_info_panel(self, game_state: GameState) -> None:
        """Updates info panel to represent current game state."""
        self._info_panel.update(game_state)
    
    def update_turn_history(
            self, turn: int, players: bool,  score: int = 0,
            formed_words: list[str] | None = None
        ) -> None:
        """Adds most recent move to turn history."""
        self._info_panel.update_turn_history(
           turn, players, score, formed_words 
        )
    
    def disable_for_bot_move(self, disable: bool) -> None:
        """Disableds buttons so user cannot interfere with bot move."""
        self._game_area.set_buttons_disabled(disable)
        self._button_console.set_buttons_disabled(disable)
    
    def connect_to_controller(self, controller):
            # Connect slots to button panel
        self._game_area.skipPressed.connect(controller._on_skip)
        self.game_area.swapPressed.connect(controller._on_swap)
        self.game_area.submitPressed.connect(controller._on_submit)

        # Connect slots to game events
        self.game_area.tilePlaced.connect(
            controller._on_tile_placed
        )
        self.game_area.tileRemoved.connect(
            controller._on_tile_removed
        )

        # Connect slots to button console
        self.button_console.infoPressed.connect(
            self.open_game_info
        )
        self.button_console.dictPressed.connect(
            self.open_dictionary
        )
        self.button_console.peekPressed.connect(
            controller._see_bot_rack
        )
        self.button_console.hintPressed.connect(
            controller._get_hint
        )

    def _load_qss(self) -> str:
        """
        Returns string joining QSS from all QSS files, inserting 
        palette values.
        """
        return "\n".join(
            Path(path).read_text(encoding="utf-8").format(**PALETTE)
            for path in self.STYLE_PATHS
        )