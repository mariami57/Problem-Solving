from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = {}

        for i in range(len(list1)):
            if list1[i] in list2:
                if list1[i] in index_sum:
                    index_sum[list1[i]] += i + list2.index(list1[i])
                else:
                    index_sum[list1[i]] = i + list2.index(list1[i])

        sorted_sum = dict(sorted(index_sum.items(), key=lambda x: x[1]))
        min_keys = [k for k, v in sorted_sum.items() if v==min(sorted_sum.values())]

        return min_keys

print(Solution().findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))



