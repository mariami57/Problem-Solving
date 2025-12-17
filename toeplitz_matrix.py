from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        top_left = (-1, -1)

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            diag_row = r + top_left[0]
            if 0 <= diag_row < rows:
                for c in range(cols):
                    diag_col = c + top_left[1]
                    if 0 <= diag_col < cols:
                        if matrix[diag_row][diag_col] != matrix[r][c]:
                            return False
        return True

print(Solution().isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(Solution().isToeplitzMatrix(matrix = [[1,2],[2,2]]))