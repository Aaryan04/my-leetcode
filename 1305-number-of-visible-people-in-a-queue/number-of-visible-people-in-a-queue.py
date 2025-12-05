class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        #             i       j 
        # heights = [10,6,8,5,11,9]
        #             0,1,2,3, 4,5
        # ans = [3, 1, 2, 1, 1, 0]
        n = len(heights)
        ans = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            height = heights[i]
            cnt = 0
            # While there are people to the right shorter than current person:
            # They are visible, and the current person blocks them for others.

            while stack and stack[-1] < height:
                stack.pop()
                cnt += 1

            if stack:
                cnt += 1

            ans[i] = cnt
            stack.append(height)
        return ans

            