class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # RESOLVE THIS PROBLEM AGAIN
        
        ROWS = len(board)
        COLS = len(board[0])
        ships = 0

        # we will just cnt the top left of each ship grp, if left or up cell have a ship then its not a ship
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != 'X':
                    continue
                if (r > 0 and board[r-1][c] == 'X'):
                    continue
                if (c > 0 and board[r][c-1] == 'X'):
                    continue
                ships += 1

        return ships