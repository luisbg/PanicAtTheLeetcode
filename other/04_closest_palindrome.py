"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.
"""

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        # save the original as an integer to compare latter
        orig = int(n)

        # edge candidates: one with fewer digits, one with more digits
        candidates = set()
        candidates.add(10 ** (length - 1) - 1)  # e.g. 999 for length 3
        candidates.add(10 ** length + 1)        # e.g. 1001 for length 3

        # build palindromes from prefix - 1, prefix, prefix + 1
        # prefix is the first half (and middle, if odd length)
        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        for delta in (-1, 0, 1):
            p = prefix + delta
            if p <= 0:
                continue
            s = str(p)
            if length % 2 == 0:
                # even length: mirror whole s
                pal = s + s[::-1]
            else:
                # odd length: mirror all but last char
                pal = s + s[-2::-1]
            candidates.add(int(pal))

        # choose the best candidate:
        #     not equal to orig
        #     minimal absolute difference
        #     if tie, minimal value
        best = None
        for c in candidates:
            if c == orig:
                continue
            diff = abs(c - orig)
            if best is None:
                best = c
            else:
                best_diff = abs(best - orig)
                if diff < best_diff or (diff == best_diff and c < best):
                    best = c

        return str(best)
