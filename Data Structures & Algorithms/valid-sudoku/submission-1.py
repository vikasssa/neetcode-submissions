class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        # 3x3 grid of sets for sub-boxes
        grids = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Directly access the 2D set using row and col integer division
                grid_r, grid_c = r // 3, c // 3

                if val in rows[r] or val in cols[c] or val in grids[grid_r][grid_c]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                grids[grid_r][grid_c].add(val)

        return True