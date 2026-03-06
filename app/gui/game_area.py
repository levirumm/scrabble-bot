from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFrame, QHBoxLayout, QGridLayout,
    QPushButton, QGraphicsOpacityEffect
)
from PySide6.QtCore import (
    Qt, QSize, QMimeData, Signal, QEvent, QObject,
    QTimer
)
from PySide6.QtGui import (
    QPainter, QFont, QDrag, QPixmap, QIcon, 
    QMouseEvent
)
from app.gui.layout.ui_scrabble_view import Ui_ScrabbleView
from app.model.types import (
    CellType, Tile, TilePlacement, SlotMetrics
)
from app.model.constants import (
    BOARD_SIZE, RACK_SLOTS, JOKER_CHAR
)
from app.gui.effects import get_drop_shadow
from pathlib import Path


class GameArea(QObject):
    """
    Represents playable area of applications, including Scrabble 
    board, letter rack, and button panel.
    """
    # Button panel
    resignPressed = Signal()
    skipPressed = Signal()
    swapPressed = Signal()
    submitPressed = Signal()

    # Tile events
    tilePlaced = Signal(int, int, Tile)
    tileRemoved = Signal(int, int)
    letterRequired = Signal(QObject)

    def __init__(
            self, cell_types: list[list[CellType]], 
            ui = Ui_ScrabbleView()
        ) -> None:
        super().__init__()
        self._ui: Ui_ScrabbleView = ui

        # Set widget properties for styling
        self._ui.button_container.setProperty("role", "bg")

        # Scrabble board 
        self._board = BoardWidget(
            cell_types=cell_types,
            border=self._ui.board_container,
            layout=self._ui.grid_layout
        )

        # Letter rack (recall button + tiles)
        self._rack = LetterRack(
            layout=self._ui.letter_rack_layout,
            container=self._ui.letter_rack
        )

        # Button panel (Resign, Skip, Swap, Submit)
        self._render_button_panel()

        # Connect slots to button panel signals
        self._skip_button.clicked.connect(self._on_skip)
        self._swap_button.clicked.connect(
            lambda: self.swapPressed.emit()
        )
        self._submit_button.clicked.connect(
            lambda: self.submitPressed.emit()
        )

        # Connect slots to tile signals
        self._rack.letterRequired.connect(
            self._on_letter_required
        )
        self._board.tilePlaced.connect(self._tile_placed)
        self._board.tileRemoved.connect(self._tile_removed)
    
    def apply_move(
            self, placements: list[TilePlacement], 
            pending: bool = True
        ) -> None:
        self._board.apply_move(placements, pending)
    
    def show_hint_preview(self, placements: list[TilePlacement]) -> None:
        self._board.show_hint_preview(placements)
    
    def remove_hint_preview(self) -> None:
        self._board.remove_hint_preview()
    
    def update_player_rack(
            self, new_tiles: list[Tile], 
            used_tiles: list[Tile] | None = None,
            racked: bool = False, hint: bool = False
        ) -> None:
        self._rack.update(
            new_tiles, used_tiles, racked, hint
        )
    
    def update_pending(self) -> None:
        self._board.update_pending()
    
    def recall(self) -> None:
        self._rack.recall()

    def _on_skip(self) -> None:
        self.skipPressed.emit()
    
    def _tile_placed(self, row: int, col: int, tile: Tile) -> None:
        self.tilePlaced.emit(row, col, tile)
    
    def _tile_removed(self, row: int, col: int) -> None:
        self.tileRemoved.emit(row, col)
    
    def _on_letter_required(self, tile: "JokerTile") -> None:
        self.letterRequired.emit(tile)
    
    def _render_button_panel(self) -> None:
        self._resign_button = self._ui.resign_button
        self._skip_button = self._ui.skip_button
        self._swap_button = self._ui.swap_button
        self._submit_button = self._ui.submit_button

        self._resign_button.setProperty("role", "button")
        self._skip_button.setProperty("role", "button")
        self._swap_button.setProperty("role", "button")
        self._submit_button.setProperty("role", "button")
        self._submit_button.setProperty("variant", "green")


class BoardWidget(QWidget):
    """
    Represents the graphical Scrabble board composed of cell 
    widgets and containing tile widgets.
    """
    tilePlaced = Signal(int, int, Tile)
    tileRemoved = Signal(int, int)
    
    def __init__(
            self, cell_types: list[list[CellType]], 
            border: QFrame, layout: QGridLayout
        ) -> None:
        super().__init__()
        self._cells: list[list[CellWidget]] = (
            self._render_board(cell_types, border, layout)
        )
        self._pending_tiles: list[TileWidget] = []
        self._hint_tiles: dict = {}

    @property
    def cells(self) -> list[list["CellWidget"]]:
        return self._cells

    def update_pending(self) -> None:
        """Sets tiles in pending to normal style."""
        for tile_widget in self._pending_tiles:
            tile_widget.set_pending(False)
    
    def remove_hint_preview(self) -> None:
        """Deletes tile widgets composing hint."""
        for tile_widget in self._hint_tiles.keys():
            tile_widget.deleteLater()
            tile_widget.slot.clear()
        self._hint_tiles: dict = {}
    
    def apply_move(
            self, tiles: list[TilePlacement], 
            pending: bool = True
        ) -> None:
        """
        Renders tiles widgets from move. Uses pending 
        styling unless otherwise stated.
        """
        tile_widgets = self._render_tiles(tiles)
        self._pending_tiles: list[TileWidget] = []
        self._pending_tiles.extend(tile_widgets)

        for tile in self._pending_tiles:
            tile.set_pending(True)
    
    def show_hint_preview(self, tiles: list[TilePlacement]) -> None:
        self._hint_tiles: dict = {}

        tile_widgets = self._render_tiles(tiles)

        for tile in tile_widgets:
            effect = QGraphicsOpacityEffect()
            effect.setOpacity(0.7)
            tile.setGraphicsEffect(effect)
            self._hint_tiles[tile] = effect

    def _render_tiles(
            self, tiles: list[TilePlacement]
        ) -> list["TileWidget"]: 
        """Renders and returns references to tile widgets."""
        tile_widgets: list[TileWidget] = []

        for tp in tiles:
            tile = tp.tile

            if tile.is_blank:
                tile_widget = JokerTile(tile)
            else:
                tile_widget = TileWidget(tile)

            cell = self._cells[tp.row][tp.col]
            cell.add_tile(tile_widget)
            tile_widget.disable()
            tile_widgets.append(tile_widget)
        return tile_widgets

    def _tile_placed(self, row: int, col: int, tile: Tile) -> None:
        """
        Emits signal. If bot's move in pending, sets tile widgets
        to normal.
        """
        self.tilePlaced.emit(row, col, tile)

        if self._pending_tiles:
            # Set bot's pending tiles to normal
            self.update_pending()
    
    def _tile_removed(self, row: int, col: int) -> None:
        self.tileRemoved.emit(row, col)
    
    def _render_board(
            self, cell_types: list[list[CellType]], 
            border: QFrame, layout: QGridLayout
        ) -> list[list["CellWidget"]]:
        border.setProperty("variant", "board_border")
        layout.setSpacing(1)

        cells: list[list[CellWidget]] = []

        for row in range(BOARD_SIZE):
            row = self._render_row(cell_types, row, layout)
            cells.append(row)
        return cells
    
    def _render_row(
            self, cell_types: list[list[CellType]], 
            row: int, layout: QGridLayout
        ) -> list["CellWidget"]:
        row_cells: list[CellWidget] = []

        for col in range(BOARD_SIZE): 
            cell_type = cell_types[row][col]
            cell = CellWidget(row, col, cell_type)
            row_cells.append(cell)

            layout.addWidget(cell, row, col)

            cell.tilePlaced.connect(self._tile_placed)
            cell.tileRemoved.connect(self._tile_removed)
        return row_cells


class TileMetrics(QObject):
    """
    Computes and stores metrics of tiles based on slot size 
    for fast rendering.
    """
    CURSOR_PATH = (
        Path(__file__).parent.parent.parent 
        / "assets" / "closed_hand_cursor.png"
    )
    LETTER_SIZE_RATIO: float = 2.5
    POINTS_SIZE_RATIO: int = 5
    SCORE_OFFSET_RATIO: int = 10
    LETTER_OFFSET_RATIO: int = 15
    CURSOR_SIZE: int = 32

    def __init__(self) -> None:
        self._metrics: dict[int, SlotMetrics] = {}
        self._closed_hand_pixmap = (
            QPixmap(self.CURSOR_PATH).scaled(
            self.CURSOR_SIZE, self.CURSOR_SIZE, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        ))
    
    @property
    def closed_hand_pixmap(self) -> QPixmap:
        return self._closed_hand_pixmap
    
    def slot_metrics(self, slot_size: int) -> SlotMetrics:
        """
        Checks cache for dimensions. If not there, computes 
        and stores.
        """
        if slot_size in self._metrics:
            return self._metrics[slot_size]
        
        self._metrics[slot_size] = SlotMetrics(
            letter_font=QFont(
                "Arial",
                int(slot_size / self.LETTER_SIZE_RATIO),
                QFont.Weight.Bold
            ),
            score_font=QFont(
                "Arial",
                int(slot_size / self.POINTS_SIZE_RATIO),
                QFont.Weight.Bold
            ),
            letter_offset=slot_size // self.LETTER_OFFSET_RATIO,
            score_x_offset=slot_size // self.SCORE_OFFSET_RATIO,
            score_y_offset=(
                (slot_size // self.SCORE_OFFSET_RATIO) // 2
            )
        )
        return self._metrics[slot_size]


class TileWidget(QFrame):
    """
    Represents a draggable Scrabble tile that can occupy 
    a TileSlot.
    """
    doubleClicked = Signal(QObject)

    _tile_metrics: TileMetrics | None = None

    @classmethod
    def _get_metrics(cls, slot_size: int) -> SlotMetrics:
        if cls._tile_metrics is None:
            cls._tile_metrics = TileMetrics()
        return cls._tile_metrics.slot_metrics(slot_size)

    @classmethod
    def _get_cursor(cls) -> QPixmap:
        if cls._tile_metrics is None:
            cls._tile_metrics = TileMetrics()
        return cls._tile_metrics.closed_hand_pixmap
    
    def __init__(self, tile: Tile):
        super().__init__()
        self._tile: Tile = tile
        self._slot: TileSlot | None = None
        self._disabled: bool = False

        # Set cursor to open hand when hovered
        self.setCursor(Qt.CursorShape.OpenHandCursor)
    
    @property
    def tile(self) -> Tile:
        return self._tile
    
    @property
    def slot(self) -> "TileSlot | None":
        return self._slot

    def disable(self) -> None:
        """
        Makes tile undraggable and use arrow cursor when 
        hovered.
        """
        self._disabled = True
        self.setCursor(Qt.CursorShape.ArrowCursor)
    
    def set_pending(self, is_pending: bool) -> None:
        """Changes state of widget and polishes."""
        if is_pending:
            self.setProperty("state", "pending")
        else:
            self.setProperty("state", "normal")
        self.style().polish(self)
    
    def accept_new_slot(self, slot: "TileSlot") -> None:
        """Resizes and redraw tile widget to fit new slot."""
        old_slot = self._slot
        self._slot = slot

        if old_slot:
            # Remove tile from old slot
            old_slot.clear()
            
            if self._slot.slot_size == old_slot.slot_size:
                # Same size slot, no need to resize
                return 

        # Resize tile to fit new slot
        size = self._slot.slot_size
        self.setFixedSize(size, size)
    
    def paintEvent(self, event: QEvent):
        """Renders the letter and point value on the tile."""
        if not self._slot or self._tile.letter == JOKER_CHAR:
            # No slot to be painter in or
            # unset joker whic does not get labels
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect()
        metrics = self._get_metrics(self._slot.slot_size)

        # Draw letter label (centered and shifted up slightly)
        letter_rect = rect.adjusted(
            0, -metrics.letter_offset, 0, -metrics.letter_offset
        )
        painter.setFont(metrics.letter_font)
        painter.drawText(
            letter_rect, Qt.AlignmentFlag.AlignCenter, 
            self._tile.letter
        )

        # Draw points label (bottom-right corner)
        score_rect = rect.adjusted(
            0, 0, -metrics.score_x_offset, -metrics.score_y_offset
        )
        painter.setFont(metrics.score_font)
        painter.drawText(
            score_rect, Qt.AlignmentFlag.AlignRight | 
            Qt.AlignmentFlag.AlignBottom, 
            str(self._tile.points)
        )

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Ignores press if disabled, else calls press function."""
        if self._disabled:
            return
        self._on_mouse_press(event)
    
    def _on_mouse_press(self, event: QMouseEvent) -> None:
        """Starts drag on left click. Extended by Joker tile."""
        if event.button() == Qt.MouseButton.LeftButton:
            self._start_drag(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        """Allows user to recall tile on double click."""
        if self._disabled:
            return
        if event.button() == Qt.MouseButton.LeftButton:
            self.doubleClicked.emit(self)

    def _start_drag(self, event) -> None:
        """
        Creates a drag pixmap. Hides tile while dragged and 
        shows once in dropped in slot.
        """
        # Create drag object
        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)

        # Set cursor to closed hand
        cursor = self._get_cursor()
        drag.setDragCursor(cursor, Qt.DropAction.MoveAction)
        drag.setDragCursor(cursor, Qt.DropAction.IgnoreAction)
        drag.setDragCursor(cursor, Qt.DropAction.CopyAction)

        # Render widget as drag pixmap
        dpr = self.devicePixelRatioF()
        pixmap = QPixmap(self.size() * dpr)
        pixmap.setDevicePixelRatio(dpr)
        pixmap.fill(Qt.GlobalColor.transparent)
        self.render(pixmap)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.position().toPoint())

        self.hide() # Hide original widget to prevent duplication
        drag.exec(Qt.DropAction.MoveAction)
        self.show() # Show widget in new position


class JokerTile(TileWidget):
    """
    Tile widget which allows user to select it's letter. 
    Appears blank until set by user.
    """
    letterRequired = Signal(TileWidget)

    def __init__(self, tile: Tile) -> None:
        super().__init__(tile)
    
    def _on_mouse_press(self, event: QMouseEvent) -> None:
        """Emits signal to open letter selection menu."""
        super()._on_mouse_press(event)
        if event.button() == Qt.MouseButton.RightButton:
            pass
            self.letterRequired.emit(self)
        
    def accept_new_slot(self, slot: "TileSlot") -> None:
        """
        Opens letter selection menu if blank tile is placed 
        on board.
        """
        super().accept_new_slot(slot)
        if (self._tile.letter == JOKER_CHAR
            and isinstance(self.slot, CellWidget)
        ):
            # Delay so tile renders before letter select opens
            QTimer.singleShot(
                1, lambda: self.letterRequired.emit(self)
            )
        
    def update_letter(self, letter: str) -> None:
        """Redraws tile to display given letter."""
        self._tile.letter = letter
        self.update()


class TileSlot(QFrame):
    """
    Represents a slot which can accept a Scrabble tile. Parent 
    class of RackSlot and CellWidget.
    """
    def __init__(self, size: int) -> None:
        super().__init__()
        self._size: int = size
        self._occupied: bool = False

        self.setAcceptDrops(True)

        # Layout to hold tile
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)
        
    @property
    def slot_size(self) -> int:
        return self._size

    def set_occupied(self, is_occupied: bool) -> None:
        self._occupied = is_occupied

    def add_tile(self, tile: TileWidget) -> None:
        """Adds tile to layout and updates tile's slot."""
        self._layout.addWidget(tile)
        self._occupied = True
        tile.accept_new_slot(self)

    def clear(self) -> None:
        """Sets occupied flag to false and removes hover."""
        self._occupied = False
        self._set_hover(False)
    
    def dragEnterEvent(self, event: QEvent):
        """Sets slot to hover styling."""
        self._set_hover(True)
        event.accept()
    
    def dragLeaveEvent(self, event: QEvent):
        """Removes hover styling."""
        self._set_hover(False)

    def dropEvent(self, event):
        """Reject drop if occupied. Else, add tile to layout."""
        if self._occupied:
            return
        tile: TileWidget = event.source()
        event.accept()
        self._on_drop(tile)
    
    def _on_drop(self, tile: TileWidget) -> None:
        """Trivial function to be extended by child classes."""
        self.add_tile(tile)
    
    def _set_hover(self, hover: bool) -> None:
        """Adds or removes hover styling."""
        self.setProperty("tile_hover", hover)
        self.style().polish(self)


class CellWidget(TileSlot):
    """Represents a single cell in the Scrabble board."""
    CELL_SIZE: int = 31

    tilePlaced = Signal(int, int, Tile)
    tileRemoved = Signal(int, int)

    def __init__(
            self, row: int, col: int, cell_type: CellType
        ) -> None:
        super().__init__(self.CELL_SIZE)
        self._row = row
        self._col = col

        self._render_cell(cell_type)
    
    def add_tile(self, tile: TileWidget) -> None:
        """Adds tile and changes tile to pending styling."""
        super().add_tile(tile)
        tile.set_pending(True)
    
    def clear(self) -> None:
        super().clear()
        self.tileRemoved.emit(self._row, self._col)
    
    def _on_drop(self, tile: TileWidget) -> None:
        super()._on_drop(tile)
        self.tilePlaced.emit(
            self._row, self._col, tile.tile
        )    
    
    def _render_cell(self, cell_type: CellType) -> None:
        self.setFixedSize(QSize(self.CELL_SIZE, self.CELL_SIZE))
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setProperty("variant", cell_type.value)


class RackSlot(TileSlot):
    """
    Represents a slot in the letter rack which can hold 
    a Scrabble tile.
    """
    def __init__(self, size: int):
        super().__init__(size)
        self._render_slot(size)
    
    @property
    def occupied(self) -> bool:
        return self._occupied

    def add_tile(self, tile: TileWidget) -> None:
        """Adds tile and removes pending styling."""
        super().add_tile(tile)
        tile.set_pending(False)

    def _render_slot(self, size: int) -> None:
        self.setFixedSize(QSize(size, size))
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)


class LetterRack(QObject):
    """
    Represents the letter rack comprised of seven rack slots.
    """
    RECALL_ICON_PATH = (
        Path(__file__).parent.parent.parent 
        / "assets" / "down_arrow"
    )
    SLOT_SIZE: int = 40

    letterRequired = Signal(JokerTile)

    def __init__(
            self, layout: QHBoxLayout, container: QFrame
        ) -> None:
        super().__init__()

        # Apply styling properties and drop shadow to rack
        self._shadow = get_drop_shadow()
        container.setProperty("role", "rack")
        container.setGraphicsEffect(self._shadow)

        self._rack_slots: list[RackSlot] = []
        self._tiles: list[TileWidget] = []

        self._render_recall_button(layout)
        self._render_letter_rack(layout)

        self._recall_button.clicked.connect(self.recall)
    
    def recall(self) -> None:
        """Recalls all tiles on board to rack."""
        for tile in self._tiles:
            if isinstance(tile.slot, CellWidget):
                self._add_tile(tile)
    
    def update(
            self, new_tiles: list[Tile],  
            used_tiles: list[Tile] | None = None,
            racked: bool = False, hint: bool = False
        ) -> None:
        """
        Disables and removes reference to used tiles. Creates tile 
        widget for each new tile and adds to rack.
        """
        if used_tiles:
            # Remove used tiles
            for tile in used_tiles:
                self._remove_tile(tile, racked, hint)

        for tile in new_tiles:
            # Create new tiles
            if tile.is_blank:
                tile_widget = JokerTile(tile)
                # Connect to letter required signal
                tile_widget.letterRequired.connect(
                    self._on_letter_required
                )
            else:
                tile_widget = TileWidget(tile)  
            # Connect to double click for tile recall
            tile_widget.doubleClicked.connect(self._add_tile) 
            self._tiles.append(tile_widget)
            self._add_tile(tile_widget)
    
    def _add_tile(self, tile: TileWidget) -> None:
        """Adds tile widget to next available rack slot."""
        for slot in self._rack_slots:
            if not slot.occupied:
                slot.add_tile(tile)
                break

    def _remove_tile(self, tile: Tile, racked: bool, hint: bool) -> None:
        """
        Disables, sets to normal styling, and removes reference 
        to corresponding tile widget.
        """
        slot_type = RackSlot if (racked or hint) else CellWidget

        if hint and tile.is_blank:
            tile_widget = next(
                widget for widget in self._tiles 
                if widget.tile.is_blank
            )
        else:
            tile_widget = (
                next(widget for widget in self._tiles 
                if widget.tile == tile
                and isinstance(widget.slot, slot_type))
            )

        self._tiles.remove(tile_widget)

        if slot_type == CellWidget:
            tile_widget.disable()
            tile_widget.set_pending(False)
        else:
            tile_widget.slot.set_occupied(False) # type: ignore
            tile_widget.deleteLater()
    
    def _on_letter_required(self, tile: JokerTile) -> None:
        self.letterRequired.emit(tile)
    
    def _render_recall_button(self, layout: QHBoxLayout) -> None:
        self._recall_button = QPushButton()
        self._recall_button.setFixedSize(
            QSize(self.SLOT_SIZE, self.SLOT_SIZE)
        )
        self._recall_button.setIcon(
            QIcon(str(self.RECALL_ICON_PATH))
        )
        self._recall_button.setProperty("role", "recall")
        layout.addWidget(self._recall_button)
        self._recall_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )
        self._recall_button.setToolTip(
            "Recall tiles to letter rack"
        )
    
    def _render_letter_rack(self, layout: QHBoxLayout) -> None:
        for _ in range(RACK_SLOTS):
            slot = RackSlot(self.SLOT_SIZE)
            layout.addWidget(slot)
            self._rack_slots.append(slot) 