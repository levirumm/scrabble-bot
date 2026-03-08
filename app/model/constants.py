BOARD_SIZE: int = 15 # Standard Scrabble board is 15 x 15
RACK_SLOTS: int = 7  # Max tiles in players letter rack
JOKER_CHAR: str = "?"
BINGO_BONUS: int = 50
MAX_CONSECUTIVE_SKIPS: int = 4

LETTER_SCORES: dict[str, int] = {
    # Maps letters to their points value
    "A": 1, "B":  3, "C": 3, "D": 2, "E": 1, "F": 4, 
    "G": 2, "H": 4, "I": 1,"J": 8, "K": 5, "L": 1, 
    "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10,"R": 1,
    "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, 
    "Y": 4, "Z": 10, JOKER_CHAR: 0
}

LETTER_DISTRIBUTION: dict[int, list[str]] = {
    # Maps frequency to letters that occur at that frequency
    1: ["J","K","Q","X","Z"],
    2: ["B","C","F","H","M","P","V","W","Y", JOKER_CHAR],
    3: ["G"],
    4: ["D","L","S","U"],
    6: ["N","R","T"],
    8: ["O"],
    9: ["A","I"],
    12: ["E"]
}