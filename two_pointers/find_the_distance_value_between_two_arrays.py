from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        i,j, count = 0, 0, 0

        while i < len(arr1) and j < len(arr2):
            if abs(arr1[i] - arr2[j]) > d:
                j += 1
            elif abs(arr1[i] - arr2[j]) <= d:
                j = 0
                i += 1
            if j == len(arr2):
                i += 1
                j = 0
                count += 1

        return count

print(Solution().findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
print(Solution().findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))
print(Solution().findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))




