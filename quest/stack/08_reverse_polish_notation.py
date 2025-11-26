class Solution(object):
    def is_operator(self, token):
        return token == "+" or token == "-" or token == "*" or token == "/"

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if not self.is_operator(t):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(float(a) / b)) # make sure we truncate toward zero
        
        return stack.pop()


# If you’re running this as Python 3, "/" case is simply: int(a / b),
# because / gives you a float and int() truncates toward zero.
