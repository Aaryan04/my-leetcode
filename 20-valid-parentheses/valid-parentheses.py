class Solution:
    def isValid(self, s: str) -> bool:
        match = {')' : '(', 
                 ']' : '[', 
                 '}' : '{'}
        stack = []

        for char in s:
            if char in match:
                x = stack.pop() if stack else '#'
                if x != match[char]:
                    return False
            else:
                stack.append(char)
                
        return False if stack else True