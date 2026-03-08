from PySide6.QtWidgets import (
    QDialog, QPushButton, QLabel, QFrame, QWidget,
    QGraphicsEffect, QGraphicsOpacityEffect
)
from PySide6.QtCore import (
    Qt, Signal, QEvent, QObject, QPropertyAnimation, 
    QTimer, QPoint
)
from PySide6.QtGui import QPixmap
from app.gui.layout.ui_letter_select_menu import (
    Ui_letter_select
)
from app.model.types import Tile, ToastType
from app.gui.layout.ui_tile_swap import Ui_tile_swap
from app.gui.layout.ui_bot_peek import Ui_bot_peek
from app.gui.layout.ui_dictionary import Ui_dictionary
from app.gui.layout.ui_hint_menu import Ui_hint_menu
from app.gui.layout.ui_game_info import Ui_game_info
from app.gui.effects import get_drop_shadow
from app.gui.game_area import (
    TileWidget, JokerTile, TileSlot
)
from app.model.word_structures import DICTIONARY
from pathlib import Path
from typing import Protocol


class PopUpMenu(Protocol):
    """
    Protocol for pop ups used by style function.
    """
    frame: QFrame
    title: QLabel


def style_pop_up(
        window: QDialog, ui: PopUpMenu, modal: bool
    ) -> QGraphicsEffect:
    """
    Applies styling common to pop ups. Returns reference 
    to shadow effect to allow reference storage.
    """
    flags = Qt.WindowType.FramelessWindowHint
    flags |= (
        Qt.WindowType.Dialog if modal else 
        Qt.WindowType.Popup | 
        Qt.WindowType.NoDropShadowWindowHint
    )
    window.setWindowFlags(flags)
    window.setAttribute(
        Qt.WidgetAttribute.WA_TranslucentBackground
    )

    # Apply common styling properties and drop shadow
    ui.frame.setProperty("role", "top_card")
    ui.title.setProperty("role", "sub_heading")
    shadow = get_drop_shadow()
    ui.frame.setGraphicsEffect(shadow)

    return shadow


def render_icon(
        label: QLabel, icon_path: Path, 
        role_str: str
    ) -> None:
    """
    Adds icon of given path to label and applies styling
    properties.
    """
    icon = QPixmap(str(icon_path))
    label.setPixmap(icon)
    label.setScaledContents(True)
    label.setProperty("role", role_str)


class ToastManager(QObject):
    """Manages toasts to avoid stacking."""

    def __init__(self) -> None:
        super().__init__()
        self._toast: Toast | None = None

    def show_toast(self, parent, message: str, type: ToastType) -> None:
        """Creates a toast instance, deleting previous if exists."""
        if self._toast:
            self._toast.hide()
        self._toast = Toast(parent, message, type)
        self._toast.toastClosed.connect(self._close_toast)

    def _close_toast(self) -> None:
        self._toast = None


class Toast(QObject):
    """
    Toast which appears at top-middle of window and fades 
    away after a couple seconds.
    """
    TOAST_DURATION: int = 1200 # miliseconds

    toastClosed = Signal()

    def __init__(
            self, parent, message: str, type: ToastType
        ) -> None:
        super().__init__()
        # Create QLabel to act as toast
        self._toast = QLabel(message, parent)
        self._toast.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._toast.setProperty("role", "toast")
        self._toast.setProperty("variant", type.value)
        self._toast.adjustSize()
        
        # Define fade out effect
        effect = QGraphicsOpacityEffect(self._toast)
        effect.setOpacity(1.0)
        self._toast.setGraphicsEffect(effect)
        self._fade = QPropertyAnimation(
            effect, b"opacity", self._toast
        )
        self._fade.setStartValue(1)
        self._fade.setEndValue(0)
        self._fade.finished.connect(self._destroy)

        # Position self._toast in center of parent
        center = parent.rect().center()
        self._toast.move(
            center.x() - self._toast.width() // 2,
            center.y() - self._toast.height() // 2
        )
        self._toast.show()

        # Initiate fade after delay
        QTimer.singleShot(
            self.TOAST_DURATION, self._fade.start
        )
    
    def hide(self) -> None:
        self._toast.hide()
        
    def _destroy(self) -> None:
        self.deleteLater()
        self.toastClosed.emit()


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


class LetterSelect(QDialog, Ui_letter_select):
    """
    Modal dialog menu allowing user to select the letter 
    of a Joker tile.
    """
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

        # Render graphics elements
        self._shdw = style_pop_up(self, ui, modal=True)
        render_icon(
            ui.joker_label, self.JOKER_PATH,
            role_str="joker_icon"
        )
        self._render_keyboard(ui) 
    
    @property
    def selected_letter(self) -> str | None:
        return self._selected_letter

    def _on_select(self, letter: str) -> None:
        """Sets selected letter and closes dialog."""
        self._selected_letter = letter
        self.accept()

    def _render_keyboard(self, ui: Ui_letter_select) -> None:
        """Renders grid of letter buttons."""
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
    
    def reject(self) -> None:
        """
        Overrides reject method to prevent user escaping 
        without selecting letter.
        """
        pass


class TileSwap(QDialog, Ui_tile_swap):
    """
    Pop up menu allowing user to select tiles to swap.
    """
    SWAP_PATH = (
        Path(__file__).parent.parent.parent 
        / "assets" / "swap.png"
    )

    def __init__(self, parent, tiles: list[Tile]) -> None:
        super().__init__(parent)
        ui = Ui_tile_swap()
        ui.setupUi(self)

        # Use set of slots as slots are hashable
        self._selected: set[TileSlot] = set()
        self._slot_map: dict[TileSlot, TileWidget] = {}

        self._render_window(ui)
        self._render_tiles(ui, tiles)
        self._update()

        self._swap_button.clicked.connect(
            lambda: self.accept()
        )
        self._cancel_button.clicked.connect(
            lambda: self.reject()
        )
    
    @property
    def selected(self) -> list[Tile]:
        """Exposes list of selected tiles."""
        selected = []
        for slot in self._selected:
            tile_widget = self._slot_map[slot]
            selected.append(tile_widget.tile)
        return selected
    
    def eventFilter(self, obj: QObject, event: QEvent):
        """Catches presses to tile slots."""
        if (
            isinstance(obj, TileSlot) 
            and event.type() == QEvent.Type.MouseButtonPress
        ):
            self._on_press(obj)
        return super().eventFilter(obj, event)
    
    def _update(self) -> None:
        """Updates selection counter and swap button."""
        selected_count = len(self._selected)
        self._counter.setText(
            f"{selected_count} Selected"
        )
        self._swap_button.setDisabled(selected_count == 0)

    def _on_press(self, slot: TileSlot) -> None:
        """
        Adds or removes tile slot from selections and 
        updates styling of tile.
        """
        tile = self._slot_map[slot]
        
        if slot in self._selected:
            self._selected.remove(slot)
            tile.setProperty("state", "normal")
        else:
            self._selected.add(slot)
            tile.setProperty("state", "pending")
        tile.style().polish(tile)
        self._update()

    def _render_window(self, ui: Ui_tile_swap) -> None:
        self._shadow = style_pop_up(self, ui, modal=False)

        # Swap icon
        render_icon(
            ui.swap_icon, self.SWAP_PATH, 
            role_str="swap_icon"
        )

        # Tile selection counter (under title)
        ui.selection_count.setProperty("role", "normal")
        ui.selection_count.setProperty("variant", "muted")
        self._counter = ui.selection_count

        # Buttons (swap & skip, cancel)
        self._swap_button = ui.swap_button
        self._cancel_button = ui.cancel_button
        self._cancel_button.setProperty("role", "button")
        self._swap_button.setProperty("role", "button")
        self._swap_button.setProperty("variant", "blue")

    def _render_tiles(
            self, ui: Ui_tile_swap, tiles: list[Tile]
        ) -> None:
        """
        Renders disabled tile widgets which are transparent to 
        button presses and whose slots react to presses.
        """
        layout = ui.tile_layout
        layout.addStretch()

        for t in tiles:
            slot = TileSlot(40)
            tile = (
                JokerTile(t) if t.is_blank 
                else TileWidget(t)
            )
            slot.add_tile(tile)

            # Tile will not register presses
            tile.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents
            )
            tile.disable() # Disable just to be safe

            # Event filter to slot for presses on tile
            slot.installEventFilter(self)

            layout.addWidget(slot)

            # Map slot to tile widget. 
            # Allows widget change and access to Tile
            self._slot_map[slot] = tile
        layout.addStretch()


class BotPeek(QDialog, Ui_bot_peek):
    """
    Pop up window which lets user see bot's letter rack.
    """
    EYE_PATH = (
        Path(__file__).parent.parent.parent 
        / "assets" / "spy.png"
    )

    def __init__(self, parent, tiles: list[Tile]) -> None:
        super().__init__(parent)
        ui = Ui_bot_peek()
        ui.setupUi(self)

        self._render_window(ui)
        self._render_tiles(ui, tiles)

        self._close_button.clicked.connect(
            lambda: self.accept()
        )

    def _render_window(self, ui: Ui_bot_peek) -> None:
        self._shdw = style_pop_up(self, ui, modal=False)
        self._close_button = ui.close_button
        ui.close_button.setProperty("role", "button")
        ui.close_button.setProperty("variant", "green")
    
    def _render_tiles(
            self, ui: Ui_bot_peek, tiles: list[Tile]
        ) -> None:
        layout = ui.tile_layout
        layout.addStretch()
        for t in tiles:
            slot = TileSlot(40)
            tile = (
                JokerTile(t) if t.is_blank 
                else TileWidget(t)
            )
            slot.add_tile(tile)

            # Tile will not register presses
            tile.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents
            )
            tile.disable() # Disable just to be safe
            layout.addWidget(slot)
        layout.addStretch()


class Dictionary(QDialog, Ui_dictionary):
    DICT_PATH = (
        Path(__file__).parent.parent.parent 
        / "assets" / "book-light.png"
    )

    def __init__(self, parent) -> None:
        super().__init__(parent)
        ui = Ui_dictionary()
        ui.setupUi(self)

        self._render_window(ui)

        ui.text_input.setFocus()

        self._search_button.clicked.connect(
            self._search_word
        )
        self._close_button.clicked.connect(
            lambda: self.accept()
        )
    
    def _search_word(self) -> None:
        """
        Looks up word in dictionary and update text output.
        """
        word = self._text_input.text().strip().upper()
        definition = DICTIONARY.get(word, None)

        if definition:
            self._text_output.setText(definition)
            self._text_output.setProperty("state", "normal")
            self._text_output.style().polish(self._text_output)
        else:
            self._text_output.setText("Word not found")
            self._text_output.setProperty("state", "error")
            self._text_output.style().polish(self._text_output)

    def _render_window(self, ui: Ui_dictionary) -> None:
        self._shadow = style_pop_up(self, ui, modal=False)

        # Text input
        self._text_input = ui.text_input
        ui.line.setProperty("role", "line")

        # Search button
        self._search_button = ui.search_button
        self._search_button.setProperty("role", "button")
        self._search_button.setProperty("variant", "red")

        # Text output (disabled)
        self._text_output = ui.text_output
        ui.text_output.setDisabled(True)

        # Close button
        self._close_button = ui.close_button
        self._close_button.setProperty("role", "button")
        self._close_button.setProperty("variant", "green")


class HintMenu(QDialog, Ui_hint_menu):
    """
    Dialog which asks user if they wish to accept a 
    hint or not.
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)
        ui = Ui_hint_menu()
        ui.setupUi(self)

        self._shdw = style_pop_up(self, ui, modal=False)
        ui.cancel_button.setProperty("role", "button")
        ui.play_button.setProperty("role", "button")
        ui.play_button.setProperty("variant", "blue")

        ui.play_button.clicked.connect(
            lambda:  self.accept()
        )
        ui.cancel_button.clicked.connect(
            lambda: self.reject()
        )


class GameInfo(QDialog, Ui_game_info):
    """
    Pop up menu explaining Scrabble rules, bonus cell 
    values, and bot behaviour.
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)
        ui = Ui_game_info()
        ui.setupUi(self)

        self._render_window(ui)
    
    def _render_window(self, ui: Ui_game_info) -> None:
        ui.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        ui.line.setProperty("role", "line")

        for label in (
            ui.legend_label, ui.rules_label, 
            ui.scrabble_bot_label
        ):
            label.setProperty("role", "sub_heading")
        
        for label in (
            ui.credit_label, ui.rules_text, 
            ui.scrabble_bot_text, ui.triple_letter_label, 
            ui.double_letter_label, ui.triple_word_label, 
            ui.double_word_label
        ):
            label.setProperty("role", "normal")
            label.setProperty("variant", "muted")

        ui.triple_word_cell.setProperty(
            "role", "triple_word"
        )
        ui.double_word_cell.setProperty(
            "role", "double_word"
        )
        ui.triple_letter_cell.setProperty(
            "role", "triple_letter"
        )
        ui.double_letter_cell.setProperty(
            "role", "double_letter"
        )
        self._shdw = style_pop_up(self, ui, modal=False)