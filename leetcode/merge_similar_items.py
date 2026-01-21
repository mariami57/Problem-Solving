from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.extend(items2)
        items1.sort()

        ret = []
        for val, weight in items1:
            if ret and ret[-1][0] == val:
                ret[-1][1] += weight
            else:
                ret.append([val,weight])
        return ret

print(Solution().mergeSimilarItems(items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]))
