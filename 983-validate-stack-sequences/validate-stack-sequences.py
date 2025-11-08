class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        i, j = 0, 0

        while i < len(pushed) and j < len(popped):
            stack.append(pushed[i]) 
            i += 1
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            print(stack)
            
        while stack and j < len(popped):
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
        return True

