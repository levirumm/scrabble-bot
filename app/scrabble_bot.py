from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from app.gui.view import ScrabbleView
from app.controller.controller import ScrabbleController
from app.model.model import ScrabbleModel
from pathlib import Path


class ScrabbleBot(QApplication):
    """
    Main application class which initiates application 
    comprising model, view, and controller.
    """
    ICON_PATH = (
        Path(__file__).parent.parent / "assets" 
        / "scrabble_icon.ico"
    )

    def __init__(self) -> None:
        super().__init__()

        # Set window icon
        app_icon = QIcon(str(self.ICON_PATH))
        self.setWindowIcon(app_icon)

        # Initiate model, view, and controller
        self._model = ScrabbleModel()
        self._view = ScrabbleView(
            cell_types=self._model.board.cell_types
        )
        self._controller = ScrabbleController(
            view=self._view, model=self._model
        )

        self.exec()