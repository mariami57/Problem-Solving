from typing import List


# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         sold_count = {}
#         result = []
#         for i in range(len(mat)):
#             sold_count[i] = mat[i].count(1)
#
#         sorted_count = sorted(sold_count.items(), key=lambda x: x[1])
#
#
#         for key,v in sorted_count:
#             if len(result) < k:
#                 result.append(key)
#         return result

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)

        rows = sorted(range(m), key=lambda i: (mat[i], i))
        del rows[k:]
        return rows



print(Solution().kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))

print(Solution().kWeakestRows(mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))