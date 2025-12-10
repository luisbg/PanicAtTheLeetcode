"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""

class WordDictionary(object):
    class Node(object):
        def __init__(self):
            self.word_end = False
            self.branches = {}

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.branches:
                curr.branches[c] = self.Node()
            curr = curr.branches[c]
        curr.word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def inner_search(i, node):
            # we got to the end of word
            if i == len(word):
                return node.word_end

            c = word[i]
            if c == '.':
                # try all children
                for child in node.branches.values():
                    if inner_search(i + 1, child):
                        return True
                return False
            else:
                # normal character, follow usual trie search
                if c not in node.branches:
                    return False
                return inner_search(i + 1, node.branches[c])

        return inner_search(0, self.root)
