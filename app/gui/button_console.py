from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from app.gui.layout.ui_scrabble_view import Ui_ScrabbleView
from app.gui.effects import get_drop_shadow
from pathlib import Path


class ButtonConsole:
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
    
    def __init__(self, ui: Ui_ScrabbleView) -> None:
        self._ui = ui

        # Apply properties and drop shadow to console frame
        top_card = self._ui.button_console
        top_card.setProperty("role", "round_card")
        self._shadow = get_drop_shadow()
        top_card.setGraphicsEffect(self._shadow)

        # Information icon (i)
        info_icon = self._create_icon(
            self._ui.info_icon, "information"
        )
        # Dictionary icon (book)
        dict_icon = self._create_icon(
            self._ui.dictionary_icon, "dictionary"
        )
        # Peek icon (magnifying glass)
        peek_icon = self._create_icon(
            self._ui.peek_icon, "peek"
        )
        # Hint icon (lightbulb)
        hint_icon = self._create_icon(
            self._ui.hint_icon, "hint", small=True
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