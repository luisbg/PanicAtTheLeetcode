"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

class Trie(object):
    class Node(object):
        def __init__(self):
            self.word_end = False
            self.branches = {}

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if ch not in curr.branches:
                curr.branches[ch] = self.Node()
            curr = curr.branches[ch]
        curr.word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if ch not in curr.branches:
                return False
            curr = curr.branches[ch]
        return curr.word_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.branches:
                return False
            curr = curr.branches[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
