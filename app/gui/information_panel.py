from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QSize, Qt
from app.model.types import GameState
from app.gui.layout.ui_scrabble_view import Ui_ScrabbleView
from app.gui.layout.ui_score_box import Ui_score_box
from app.gui.layout.ui_turn_card import Ui_turn_card
from app.gui.effects import get_drop_shadow


class InfoPanel:
    """
    Right panel containing game information, including player 
    and bot points, tile tracker, and turn history.
    """
    PLAYER_NAME: str = "You"
    BOT_NAME: str = "Scrabble Bot"

    def __init__(self, ui: Ui_ScrabbleView) -> None:
        self._ui = ui

        # Set properties for QSS styling
        self._ui.info_panel_inner.setProperty(
            "role", "top_card"
        )

        # Apply drop shadow to top card
        self._shadow = get_drop_shadow()
        self._ui.info_panel_inner.setGraphicsEffect(self._shadow)

        # Score box (Player | Bot)
        self._score_board = ScoreBoard(
            self._ui, self.PLAYER_NAME, self.BOT_NAME
        )
        self._tile_tracker = self._render_tile_tracker()
        self._turn_history = TurnHistory(self._ui)
    
    def reset(self) -> None:
        self._turn_history.reset()

    def update(self, game_state: GameState) -> None:
        # Update score board
        self._score_board.update(
            game_state.player_points, game_state.bot_points
        )
        
        # Update tile tracker
        self._ui.tile_bag_tracker.setText(
            f"Tiles Remaining: {game_state.remaining_tiles}"
        )
    
    def update_turn_history(
            self, turn: int, players: bool, score: int = 0, 
            formed_words: list[str] | None = None
        ) -> None:
        name = (
            self.PLAYER_NAME if players 
            else self.BOT_NAME
        )
        if formed_words:
            self._turn_history.update(
                name, player=players, turn=turn, 
                formed_words=formed_words, 
                points=score
            )
            return
        self._turn_history.update(
            name, player=players, turn=turn
        )
        
    def _render_tile_tracker(self) -> QLabel:
        self._ui.tile_tracker_container.setProperty(
            "role", "card"
        )
        self._ui.tile_bag_tracker.setProperty(
            "role", "normal"
        )
        return self._ui.tile_bag_tracker


class Profile:
    PROFILE_SIZE: int = 27
    
    def __init__(
            self, player: bool, label: QLabel, 
            char: str
        ) -> None:
        # Set properties for styling
        variant = ("player" if player else "bot")
        label.setProperty("role", "profile")
        label.setProperty("variant", variant)

        label.setText(char)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFixedSize(
            QSize(self.PROFILE_SIZE, self.PROFILE_SIZE)
        )


class ScoreBoard:
    """Displays scores of player and Scrabble bot."""

    def __init__(
            self, ui: Ui_ScrabbleView, player_name: str, 
            bot_name: str
        ) -> None:
        ui.line.setProperty("role", "center_line")
        ui.score_box_container.setProperty(
            "role", "container"
        )
        self._player_score = ScoreBox(
            player_name, player=True
        )
        self._bot_score = ScoreBox(
            bot_name, player=False, align_right=True
        )
        ui.player_score_layout.addWidget(self._player_score)
        ui.bot_score_layout.addWidget(self._bot_score)
    
    def update(self, player_points: int, bot_points: int) -> None:
        self._player_score.update_score(player_points)
        self._bot_score.update_score(bot_points)


class ScoreBox(QWidget, Ui_score_box):
    """Represents score of individual player."""

    def __init__(
            self, name: str, player: bool, 
            align_right: bool = False
        ) -> None:
        super().__init__()
        ui = Ui_score_box()
        ui.setupUi(self)

        # Profile (uses first letter of name)
        self._profile_label = Profile(
            player, ui.profile_label, char=name[0]
        )

        # Name label (You or Scrabble Bot)
        name_label = ui.name_label
        name_label.setText(name)
        name_label.setProperty("role", "normal")

        ui.line.setProperty("role", "line")

        # Score label
        self._score_label = ui.score_label
        self._score_label.setProperty("role", "heading")

        if align_right:
            self._score_label.setAlignment(
                Qt.AlignmentFlag.AlignRight
            )
    
    def update_score(self, score: int) -> None:
        self._score_label.setText(str(score))


class TurnHistory:
    def __init__(self, ui: Ui_ScrabbleView) -> None:
        self._ui = ui

        # Remove scroll bar
        self._ui.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        # Add stretch to prevent cards from expanding
        self._ui.scroll_layout.addStretch()

        self._ui.turn_history_container.setProperty(
            "role", "container"
        )
        self._ui.turn_history_label.setProperty(
            "role", "normal"
        )
        self._ui.line_2.setProperty("role", "line")
    
    def update(
            self, name: str, player: bool, 
            turn: int, formed_words: list[str] | None = None,
            points: int = 0
        ) -> None:
        turn_card = TurnCard(
            name,  player, turn, formed_words, points
        )
        # Insert to top of scroll area
        self._ui.scroll_layout.insertWidget(0, turn_card)
    
    def reset(self) -> None:
        while self._ui.scroll_layout.count():
            item = self._ui.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        # Add stretch to prevent cards from expanding
        self._ui.scroll_layout.addStretch()


class TurnCard(QWidget, Ui_turn_card):
    def __init__(
            self, name: str, player: bool, 
            turn: int, formed_words: list[str] | None = None,
            points: int = 0
        ) -> None:
        super().__init__()
        ui = Ui_turn_card()
        ui.setupUi(self)
        
        # Profile (uses first letter of name)
        self._profile_label = Profile(
            player, ui.profile_label, char=name[0]
        )

        # Name label (You or Scrabble Bot)
        ui.name_label.setText(name)
        ui.name_label.setProperty("role", "normal")

        # Turn label
        ui.turns_label.setText(f"Turn #{turn}")
        ui.turns_label.setProperty("role", "small")
        ui.turns_label.setProperty("variant", "muted")

        if not formed_words:
            self.setProperty("variant", "skip")
            # Points label
            ui.points_label.setText(f"Skip")
            ui.points_label.setProperty("role", "normal")
            ui.points_label.setProperty("variant", "warning")
            return
        
        # List of formed words
        for word in sorted(formed_words, key=len, reverse=True):
            label = QLabel(word.upper())
            label.setProperty("role", "sub_heading")
            ui.word_list_layout.addWidget(label)
        
        # Points label
        ui.points_label.setText(f"{points} pts")
        ui.points_label.setProperty("role", "sub_heading")
        ui.points_label.setProperty("variant", "muted")