from typing import List


# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         rated = sorted(list(set(arr)))
#         ranks = []
#
#         for num in arr:
#             r = rated.index(num) + 1
#             ranks.append(r)
#         return ranks

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rated = sorted(set(arr))

        rank_map = {num: i+1 for i, num in enumerate(rated)}

        return [rank_map[num] for num in arr]

print(Solution().arrayRankTransform([40,10,20,30]))
print(Solution().arrayRankTransform([100,100,100]))
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))
