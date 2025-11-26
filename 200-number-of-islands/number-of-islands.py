class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # right, up, left, down
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r,c):
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    dfs(nr, nc)
        

        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    dfs(r,c)
                    cnt += 1
        return cnt

        

