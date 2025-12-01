class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # right, up, left, down
        ROWS = len(grid)
        COLS = len(grid[0])

        max_area = 0
        def dfs(r,c):
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
            return area
             

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
