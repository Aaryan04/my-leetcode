class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # 8 directions that a knight can move in
        directions = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]       

        def bfs(x, y):
            q = deque([[0, 0]])
            visited = set()
            steps = 0
            
            while q:
                qLen = len(q)
                
                for i in range(qLen):
                    cx, cy = q.popleft()
                    if [cx, cy] == [x, y]:
                        return steps

                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append([nx, ny])

                steps += 1
                
        return bfs(x,y)


                