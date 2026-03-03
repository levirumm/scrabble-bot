from PySide6.QtWidgets import (
    QDialog, QPushButton, QFrame, QGraphicsEffect
)
from PySide6.QtCore import Qt, Signal, QEvent, QObject
from PySide6.QtGui import QPixmap
from app.gui.layout.ui_letter_select_menu import (
    Ui_letter_select
)
from app.model.types import Tile
from app.gui.layout.ui_tile_swap import Ui_tile_swap
from app.gui.layout.ui_bot_peek import Ui_bot_peek
from app.gui.layout.ui_dictionary import Ui_dictionary
from app.gui.effects import get_drop_shadow
from app.gui.game_area import (
    TileWidget, JokerTile, TileSlot
)
from app.model.word_structures import DICTIONARY
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
    Pop up menu allowing user to select the letter 
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
        self._selected_letter = None

        ui = Ui_letter_select()
        ui.setupUi(self)
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

        ui.selection_count.setProperty("role", "normal")
        ui.selection_count.setProperty("variant", "muted")
        self._counter = ui.selection_count

        self._render_window(ui)
        self._render_tiles(ui, tiles)
    
        self._update()

        self._swap_button.clicked.connect(
            lambda:  self.accept()
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
        self._shadow = style_pop_up(self, ui.window_frame)
        
        # Swap icon (top of window)
        icon = QPixmap(str(self.SWAP_PATH))
        ui.swap_icon.setPixmap(icon)
        ui.swap_icon.setScaledContents(True)
        ui.swap_icon.setProperty(
            "role", "swap_icon"
        )
        ui.title.setProperty("role", "sub_heading")

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
        self._shadow = style_pop_up(self, ui.frame)
        
        # Peek icon (top of window)
        icon = QPixmap(str(self.EYE_PATH))
        ui.peek_icon.setPixmap(icon)
        ui.peek_icon.setScaledContents(True)
        ui.peek_icon.setProperty(
            "role", "peek_icon"
        )
        ui.title.setProperty("role", "sub_heading")

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

        self._search_button.clicked.connect(
            self._search_word
        )

        self._close_button.clicked.connect(
            lambda: self.accept()
        )
    
    def _search_word(self) -> None:
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
        self._shadow = style_pop_up(self, ui.frame)
        ui.title.setProperty("role", "sub_heading")

        self._text_input = ui.text_input
        ui.line.setProperty("role", "line")

        self._search_button = ui.search_button
        self._search_button.setProperty("role", "button")
        self._search_button.setProperty("variant", "red")

        self._text_output = ui.text_output
        ui.text_output.setDisabled(True)

        self._close_button = ui.close_button
        self._close_button.setProperty("role", "button")
        self._close_button.setProperty("variant", "green")