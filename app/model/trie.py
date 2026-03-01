from app.model.types import TrieNode
from pathlib import Path


class Trie:
    """
    Structure used for efficient Scrabble dictionary lookup.
    """
    WORDS_PATH = (
        Path(__file__).parent.parent / "data" / "scrabble_words.txt"
    )

    def __init__(self):
        self._root = TrieNode()

        # Insert text file words into self
        with open(self.WORDS_PATH, "r", encoding="UTF-8") as f:
            for line in f:
                self._insert(line.strip())
    
        #print(self.between_letters("TAL", ""))
    
    @property
    def root(self) -> TrieNode:
        return self._root
    
    def word_exists(self, word: str) -> bool:
        """Returns True if word exists in trie."""
        node: TrieNode = self._root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def between_letters(self, prefix: str, suffix: str) -> list[str]:
        """
        Returns the list of letters that occur between 
        a given prefix and suffix.
        """
        node: TrieNode = self._root
        between: list[str] = []

        # Iterate through prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # If not suffix, return children of node which form complete words
        if not suffix:
            return [
                char for char in node.children.keys() 
                if node.children[char].end
            ]
        
        # Iterate through suffix
        for letter in node.children:
            valid = True
            new_node = node.children[letter]
            for char in suffix:
                if char not in new_node.children:
                    valid = False
                    break
                new_node = new_node.children[char]
            if valid and new_node.end:
                between.append(letter)

        return between
    
    def _insert(self, word: str) -> None:
        """Inset a word into trie structre."""
        node: TrieNode = self._root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  
        node.end = True