from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        p_triangle = [[1]]

        for j in range(rowIndex + 1):
            dummy_row = [0] + p_triangle[-1] + [0]
            row = []
            for i in range(len(p_triangle[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i+1])
            p_triangle.append(row)


        return p_triangle[rowIndex]

print(Solution().getRow(3))
