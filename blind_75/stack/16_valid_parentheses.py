"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # one stacks for (), {}, and []
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        # run through the string
        for b in s:
            # when we see an open bracket we add to the related stack
            if b in "([{":
                stack.append(b) 

            # when we see a close bracket we remove from the related stack
            elif b in ")]}":
                # we should never try removing from an empty stack
                if not stack:
                    return False

                # bracket type removed should match
                c = stack.pop()
                if pairs[b] != c:
                    return False

        # at the end all stacks should be empty
        return not stack
