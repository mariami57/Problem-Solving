from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        new_mat = []

        for row in mat:
            for num in row:
                flatten.append(num)

        if r * c != len(flatten):
            return mat

        for row_index in range(r):
            new_mat.append(flatten[row_index * c : row_index*c + c])
        return new_mat

print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))

