class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # greedy approach
        stack = []
        i, j = 0, 0

        # loop through every single item in pushed
        for x in pushed:
            stack.append(x) 

            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
        return not stack

