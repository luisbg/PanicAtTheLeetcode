class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        operations = []
        index = 0
        for i in range(1, n + 1):
            stack.append(i)
            operations.append("Push")
            if i != target[index]:
                stack.pop()
                operations.append("Pop")
            else:
                index += 1
        
            if len(stack) == len(target):
                break
        
        return operations
