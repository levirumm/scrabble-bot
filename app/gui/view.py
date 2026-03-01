from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import QObject
from app.gui.layout.ui_scrabble_view import Ui_ScrabbleView
from app.model.types import (
    CellType, GameState, Tile, TilePlacement
)
from app.gui.palette.palette import PALETTE
from app.gui.button_console import ButtonConsole
from app.gui.game_area import GameArea
from app.gui.information_panel import InfoPanel
from app.gui.pop_ups import LetterSelect
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
            self._open_letter_select
        )

        # Open window in full screen
        self.showMaximized()
    
    @property
    def game_area(self) -> GameArea:
        """Exposes game area to controller."""
        return self._game_area
    
    def _open_letter_select(self, tile: QObject) -> None:
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
    
    def apply_bot_move(self, placements: list[TilePlacement]) -> None:
        """Adds bot's tiles to board."""
        self._game_area.apply_bot_move(placements)

    def update_player_rack(
            self, new_tiles: list[Tile], 
            used_tiles: list[TilePlacement] | None = None
        ) -> None:
        """Creates new tile widgets in player's letter rack."""
        self._game_area.update_player_rack(new_tiles, used_tiles)

    def _load_qss(self) -> str:
        """
        Returns string joining QSS from all QSS files, inserting 
        palette values.
        """
        return "\n".join(
            Path(path).read_text(encoding="utf-8").format(**PALETTE)
            for path in self.STYLE_PATHS
        )