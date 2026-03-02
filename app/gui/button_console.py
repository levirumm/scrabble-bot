from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Signal, QObject
from app.gui.layout.ui_scrabble_view import Ui_ScrabbleView
from app.gui.effects import get_drop_shadow
from pathlib import Path


class ButtonConsole(QObject):
    ICON_PATHS: dict[str, Path] = {
        "information": (
            Path(__file__).parent.parent.parent 
            / "assets" / "info.png"
        ),
        "dictionary": (
            Path(__file__).parent.parent.parent 
            / "assets" / "book.png"
        ),
        "peek": (
            Path(__file__).parent.parent.parent 
            / "assets" / "magnifying-glass.png"
        ),
        "hint": (
            Path(__file__).parent.parent.parent 
            / "assets" / "light.png"
        )
    }
    ICON_LARGE: int = 34
    ICON_SMALL: int = 30

    peekPressed = Signal()
    
    def __init__(self, ui: Ui_ScrabbleView) -> None:
        super().__init__()
    
        # Apply properties and drop shadow to console frame
        top_card = ui.button_console
        top_card.setProperty("role", "round_card")
        self._shadow = get_drop_shadow()
        top_card.setGraphicsEffect(self._shadow)

        # Information icon (i)
        info_icon = self._create_icon(
            ui.info_icon, "information"
        )
        # Dictionary icon (book)
        dict_icon = self._create_icon(
            ui.dictionary_icon, "dictionary"
        )
        # Peek icon (magnifying glass)
        peek_icon = self._create_icon(
            ui.peek_icon, "peek"
        )
        # Hint icon (lightbulb)
        hint_icon = self._create_icon(
            ui.hint_icon, "hint", small=True
        )

        peek_icon.clicked.connect(
            lambda: self.peekPressed.emit()
        )

    def _create_icon(
            self, button: QPushButton, key: str, 
            small: bool = False
        ) -> QPushButton:
        icon = QIcon(str(self.ICON_PATHS[key]))
        button.setIcon(icon)
        size = (
            self.ICON_SMALL if small 
            else self.ICON_LARGE
        )
        button.setIconSize(QSize(size, size))
        button.setProperty("role", "icon")
        return button