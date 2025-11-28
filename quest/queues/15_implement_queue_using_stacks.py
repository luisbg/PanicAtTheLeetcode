"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""

class MyQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.queue:
            tmp = []
            while len(self.queue) > 1:
                tmp.append(self.queue.pop())

            out = self.queue.pop()

            while tmp:
                self.queue.append(tmp.pop())

            return out
        else:
            return 0

    def peek(self):
        """
        :rtype: int
        """
        if self.queue:
            tmp = []
            while len(self.queue) > 1:
                tmp.append(self.queue.pop())

            out = self.queue.pop()

            self.queue.append(out)
            while tmp:
                self.queue.append(tmp.pop())

            return out
        else:
            return 0

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue

# Pushing from in to out stack only once per element, amortized O(1)
class MyFasterQueue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.out_stack:
            return self.out_stack.pop()
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

            if self.out_stack:
                return self.out_stack.pop()
            else:
                return 0

    def peek(self):
        """
        :rtype: int
        """
        if self.out_stack:
            return self.out_stack[-1]
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

            if self.out_stack:
                return self.out_stack[-1]
            else:
                return 0

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack
