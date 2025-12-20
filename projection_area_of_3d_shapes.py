from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0
        front = 0
        side = 0

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            front += max(grid[r])

            for c in range(col):
                if grid[r][c] > 0:
                    top += 1

        for c in range(col):
            side += max(grid[r][c] for r in range(row))
        return top + front + side

print(Solution().projectionArea([[1,2],[3,4]]))
print(Solution().projectionArea([[2]]))
print(Solution().projectionArea([[1,0],[0,2]]))


