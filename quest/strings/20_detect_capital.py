"""
We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        count = 0
        for c in word:
            if c.isupper():
                count += 1

        if count == 0:
            return True
        elif count == len(word):
            return True
        elif count == 1:
            return word[0].isupper()
        else:
            return False

    def pythonicDetectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (
            word.isupper() or              # ALL
            word.islower() or              # all lowercase
            (word[0].isupper() and word[1:].islower())  # First cap only
        )
