class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        n = len(board)
        for i in range(n):
            for j in range(n):
                # i are rows
                # j are columns
                num = board[i][j]
                row = rows[i]
                col = cols[j]
                grid = grids[(i//3) * 3 + (j//3)]
                if num == '.':
                    continue
                if num in row or num in col or num in grid:
                    if num in row:
                        print(f"Num {num} in row {i}: ", row)
                    elif num in col:
                        print(f"Num {num} in col {j}: ", col)
                    if num in grid:
                        print(f"Num {num} in grid {i}: ", grid)
                    return False
                row.add(num)
                col.add(num)
                grid.add(num)
        return True
