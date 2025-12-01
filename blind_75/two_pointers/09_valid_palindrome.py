"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    def isAlphanumeric(self, c):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True
        elif ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        else:
            return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        # remove non alphanumeric characters
        ns = [c.lower() for c in s if c.isalnum()]

        # run two pointers, one from beginning and one from end
        start = 0
        end = len(ns) - 1

        # run them until they met
        while start < end:
            # the should always match for it to be a palindrome
            if ns[start] != ns[end]:
                return False

            # move them towards the center
            start += 1
            end -= 1

        return True
