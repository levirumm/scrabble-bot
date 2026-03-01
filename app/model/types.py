from typing import Any
from enum import Enum, auto
from dataclasses import dataclass, field


class CellType(Enum):
    BLANK = "blank"
    DOUBLE_LETTER = "double_letter"
    TRIPLE_LETTER = "triple_letter"
    DOUBLE_WORD = "double_word"
    TRIPLE_WORD = "triple_word"


class CellState(Enum):
    EMPTY = auto() # No tile placed
    TEMPORARY = auto() # Tile placed this turn
    LOCKED = auto() # Tile committed from previous turn


@dataclass
class GameState:
    player_points: int
    bot_points: int
    remaining_tiles: int
    turn: int


@dataclass
class SlotMetrics:
    letter_font: Any
    score_font: Any
    letter_offset: int
    score_x_offset: int
    score_y_offset: int


@dataclass
class Tile:
    letter: str
    points: int
    is_blank: bool


@dataclass
class Cell:
    row: int
    col: int
    type: CellType = CellType.BLANK # Default to blank
    tile: Tile | None = None # Default to empty
    state: CellState = CellState.EMPTY # Default to empty
    col_restrictions: "CellRestriction | None" = None
    row_restrictions: "CellRestriction | None" = None


@dataclass
class AnchorCell:
    row: int
    col: int
    prefix: list["TilePlacement"]
    suffix: list["TilePlacement"]
    is_horizontal: bool


@dataclass
class CellRestriction:
    restrictions: list[str]
    cell_points: int


@dataclass
class TilePlacement:
    tile: Tile
    row: int
    col: int


@dataclass
class ValidationFlags:
    tiles_submitted: bool = False
    uses_multiple_tiles: bool = False
    uses_center_square: bool = False
    forms_straight_line: bool = False
    is_connected: bool = False
    no_gaps: bool = False
    invalid_word: str = ""


@dataclass
class ValidationResult:
    is_valid: bool = False
    reason: str = ""


@dataclass
class Move:
    placements: list[TilePlacement]
    score: int = 0


@dataclass
class MoveResult:
    move: Move
    formed_words: "FormedWords"
    validation_result: ValidationResult


@dataclass
class FormedWord:
    tiles: list[TilePlacement]
    is_horizontal: bool


@dataclass
class FormedWords:
    main_word: FormedWord | None = None
    cross_words: list[FormedWord] = field(default_factory=list)


@dataclass
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    end: bool = False