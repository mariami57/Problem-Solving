from typing import List


# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         rows = len(matrix)
#         cols = len(matrix[0])
#         result = []
#
#         for c in range(cols):
#             temp = []
#             for r in range(rows):
#                 temp.append(matrix[r][c])
#
#             result.append(temp)
#         return result


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(matrix) for _ in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res[c][r] = matrix[r][c]
        return res

print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().transpose([[1,2,3],[4,5,6]]))
