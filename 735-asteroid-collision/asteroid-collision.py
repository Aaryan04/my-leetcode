class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:
            alive = True

            while alive and a < 0 and stack and stack[-1] > 0:
                # case 1: top is smaller -> top explodes and check next
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                
                # case 2: same size -> both explode
                elif stack[-1] == abs(a):
                    stack.pop()
                    alive = False       # curr dies
                
                # case 3: top is higher -> curr explodes
                else:
                    alive = False

            # still survives then we append it  
            if alive:
                stack.append(a)

        return stack

                    

