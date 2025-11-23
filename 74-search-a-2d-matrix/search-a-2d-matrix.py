class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        top = 0
        bot = R - 1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
    
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        left = 0 
        right = C - 1

        while left <= right:
            m = (left + right) // 2
            if matrix[row][m] < target:
                left = m + 1
            elif matrix[row][m] > target:
                right = m - 1
            else:
                return True

        return False

