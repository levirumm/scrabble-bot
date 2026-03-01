from app.model.types import (
    Cell, CellType, CellState, Tile, TilePlacement
)
from app.model.constants import (
    BOARD_SIZE, LETTER_DISTRIBUTION, LETTER_SCORES, 
    JOKER_CHAR
)
from random import shuffle


class ScrabbleBoard:
    """Represents logical state of Scrabble board."""

    def __init__(self) -> None:
        self._board: list[list[Cell]] = self._initialise_board()
        self._is_blank: bool = True # Default is blank

    @property
    def board(self) -> list[list[Cell]]:
        return self._board
    
    @property
    def is_blank(self) -> bool:
        return self._is_blank
    
    @property
    def cell_types(self) -> list[list[CellType]]:
        """Returns CellType of each cell for board rendering."""
        return [
            [cell.type for cell in row] for row in self._board
        ]
    
    def reset(self) -> None:
        self._board: list[list[Cell]] = self._initialise_board()

    def place_tile(self, row: int, col: int, tile: Tile) -> None:
        """Adds tile to cell and marks cell as temporarily filled."""
        cell = self._board[row][col]
        cell.tile = tile
        cell.state = CellState.TEMPORARY

    def remove_tile(self, row: int, col: int) -> None:
        """Removes tile from cell and marks cell as empty."""
        cell = self._board[row][col]
        cell.tile = None
        cell.state = CellState.EMPTY
    
    def apply_move(self, placements: list[TilePlacement]) -> None:
        """Lock each placement to corresponding cell."""
        for tile in placements:
            cell = self._board[tile.row][tile.col]
            cell.tile = tile.tile
            cell.state = CellState.LOCKED
        
        # Change board state if blank
        if self._is_blank:
            self._is_blank = False

    def get_placed_tiles(self) -> list[TilePlacement]:
        """Returns list of TilePlacements where tiles are temporary."""
        return [
            TilePlacement(cell.tile, cell.row, cell.col) 
            for row in self._board for cell in row 
            if cell.tile and cell.state == CellState.TEMPORARY
        ]

    def _initialise_board(self) -> list[list[Cell]]:
        """Returns a 15 x 15 list of Cell objects."""
        board: list[list[Cell]] = [
            [Cell(r, c) for c in range(BOARD_SIZE)] 
            for r in range(BOARD_SIZE)
        ]
        self._set_cell_types(board)
        return board

    def _set_cell_types(self, board: list[list[Cell]]) -> None:
        """Inputs cell types of cells in scrabble board."""
        special_cells: dict[CellType, list[tuple[int, int]]] = {
            CellType.DOUBLE_LETTER: (
                [(0, 3), (0, 11), (2, 6), (2, 8), (3, 7), (6, 6)]
            ),
            CellType.TRIPLE_LETTER: [(1, 5), (1, 9), (5, 5)],
            CellType.DOUBLE_WORD: (
                [(1, 1), (2, 2), (3, 3), (4, 4), (7, 7)]
            ),
            CellType.TRIPLE_WORD: [(0, 0), (0, 7)],
        }
        last_idx = BOARD_SIZE - 1
        for cell_type, coords in special_cells.items():
            for row, col in coords:
                for r, c in (
                    (row, col), (col, last_idx - row), 
                    (last_idx - row, last_idx - col), 
                    (last_idx - col, row)
                ):
                    board[r][c].type = cell_type


class LetterBag:
    """Represents the bag of Scrabble tiles."""

    def __init__(self) -> None:
        self._letter_bag: list[str] = self._create_letter_bag()
        self._available_letters = self._letter_bag.copy()
    
    @property
    def remaining_tiles(self) -> int:
        return len(self._available_letters)
    
    def reset(self) -> None:
        self._available_letters = self._letter_bag.copy()
    
    def select(self, selections: int) -> list[Tile]:
        """
        Returns a list of randomly selected Tiles from 
        available letters.
        """
        shuffle(self._available_letters) # Order letters randomly

        # Select letters from available letters
        letters: list[str] = [
            self._available_letters.pop() 
            for _ in range(min(selections, len(self._available_letters)))
        ]
        # Return letters converted to tiles
        return [
            Tile(letter, LETTER_SCORES[letter], 
            is_blank=(letter==JOKER_CHAR)) 
            for letter in letters
        ]
            
    def _create_letter_bag(self) -> list[str]:
        """
        Returns the tile bag as a list of chars, where letters 
        appears as many times as their frequency.
        """
        return [
            char for frequency, letters in LETTER_DISTRIBUTION.items()
            for char in letters for _ in range(frequency)
        ]