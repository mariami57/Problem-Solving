from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []



        for i in range(n+1):
            bin_dig = str(bin(i)[2:])
            result.append(bin_dig.count('1'))

        return result

print(Solution().countBits(2))
print(Solution().countBits(5))