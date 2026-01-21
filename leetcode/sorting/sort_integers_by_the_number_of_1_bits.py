from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        binary = []

        for num in arr:
            count_ones = bin(num)[2:].count('1')
            binary.append((count_ones, num))

        binary.sort()

        result = []
        for count, num in binary:
            result.append(num)

        return result




print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))