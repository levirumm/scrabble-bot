from PySide6.QtWidgets import (
    QDialog, QPushButton, QFrame, QGraphicsEffect
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from app.gui.layout.ui_letter_select_menu import (
    Ui_letter_select
)
from app.model.types import Tile
from app.gui.layout.ui_tile_swap import Ui_tile_swap
from app.gui.effects import get_drop_shadow
from pathlib import Path


def style_pop_up(window: QDialog, frame: QFrame) -> QGraphicsEffect:
    """
    Applies styling common to pop ups. Returns reference to 
    shadow effect to allow reference storage.
    """
    window.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.Dialog
        )
    window.setAttribute(
        Qt.WidgetAttribute.WA_TranslucentBackground
    )
    # Apply card properties and drop shadow
    frame.setProperty("role", "top_card")
    shadow = get_drop_shadow()
    frame.setGraphicsEffect(shadow)

    return shadow


class LetterSelect(QDialog, Ui_letter_select):
    JOKER_PATH = (
        Path(__file__).parent.parent.parent 
        / "assets" / "joker.png"
    )
    ROWS: int = 4
    COLS: int = 7
    
    def __init__(self, parent):
        super().__init__(parent)
        ui = Ui_letter_select()
        ui.setupUi(self)

        self._selected_letter = None

        self._render_window(ui)
        self._render_keyboard(ui)
    
    @property
    def selected_letter(self) -> str | None:
        return self._selected_letter

    def _on_select(self, letter: str) -> None:
        self._selected_letter = letter
        self.accept() # Closes dialog

    def _render_window(self, ui: Ui_letter_select) -> None:
        self._shadow = style_pop_up(self, ui.window_frame)

        # Joker icon (top of window)
        icon = QPixmap(str(self.JOKER_PATH))
        ui.joker_label.setPixmap(icon)
        ui.joker_label.setScaledContents(True)
        ui.joker_label.setProperty(
            "role", "joker_icon"
        )
        ui.title.setProperty("role", "sub_heading")
    
    def _render_keyboard(self, ui: Ui_letter_select) -> None:
        layout = ui.letter_layout
        letter = "A"

        for i in range(self.ROWS * self.COLS):
            row = i // self.COLS
            col = i % self.COLS
            if (row, col) in [
                (self.ROWS-1, 0), (self.ROWS-1, self.COLS-1)
            ]: # Skip bottom corners
                continue

            button = LetterButton(letter)
            button.onClicked.connect(self._on_select)
            layout.addWidget(button, row, col)
            letter = chr(ord(letter) + 1)
    
    def reject(self):
        """
        Overrides reject method to prevent user escaping without 
        selecting letter.
        """
        pass


class LetterButton(QPushButton):
    """Simple button allowing user to select a letter."""
    BUTTON_WIDTH: int = 35
    BUTTON_HEIGHT: int = 45

    onClicked = Signal(str)

    def __init__(self, letter: str) -> None:
        super().__init__(letter)
        self._letter = letter

        self.setFixedSize(
            self.BUTTON_WIDTH, self.BUTTON_HEIGHT
        )
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("role", "letter_button")

        self.clicked.connect(self._on_clicked)
    
    def _on_clicked(self) -> None:
        self.onClicked.emit(self._letter)


class TileSwap(QDialog, Ui_tile_swap):
    def __init__(self, parent, tiles: list[Tile]) -> None:
        super().__init__(parent)
        ui = Ui_tile_swap()
        ui.setupUi(self)

        self._render_window(ui)

    def _render_window(self, ui: Ui_tile_swap) -> None:
        self._shadow = style_pop_up(self, ui.window_frame)
        """
        # Joker icon (top of window)
        icon = QPixmap(str(self.JOKER_PATH))
        ui.joker_label.setPixmap(icon)
        ui.joker_label.setScaledContents(True)
        ui.joker_label.setProperty(
            "role", "joker_icon"
        )"""
        ui.title.setProperty("role", "sub_heading")