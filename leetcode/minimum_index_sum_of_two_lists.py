from typing import List


# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         index_sum = {}
#
#         for i in range(len(list1)):
#             if list1[i] in list2:
#                 if list1[i] in index_sum:
#                     index_sum[list1[i]] += i + list2.index(list1[i])
#                 else:
#                     index_sum[list1[i]] = i + list2.index(list1[i])
#
#         sorted_sum = dict(sorted(index_sum.items(), key=lambda x: x[1]))
#         min_keys = [k for k, v in sorted_sum.items() if v==min(sorted_sum.values())]
#
#         return min_keys

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j,s_s in enumerate(list2):
            if s_s in index_map:
                index_sum = j + index_map[s_s]
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [s_s]
                elif index_sum == min_sum:
                    result.append(s_s)
        return result

print(Solution().findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))



