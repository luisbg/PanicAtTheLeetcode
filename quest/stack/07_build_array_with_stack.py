class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        operations = []
        index = 0
        for i in range(1, target[-1] + 1):
            operations.append("Push")
            if i != target[index]:
                operations.append("Pop")
            else:
                index += 1
        
            if index == len(target):
                break
        
        return operations
