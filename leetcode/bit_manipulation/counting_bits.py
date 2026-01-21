from typing import List


# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         result = []
#
#
#
#         for i in range(n+1):
#             bin_dig = str(bin(i)[2:])
#             result.append(bin_dig.count('1'))
#
#         return result

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        sub = 1

        for i in range(1, n+1):
            if sub * 2 == i:
                sub = i

            dp[i] = dp[i - sub] + 1

        return dp

print(Solution().countBits(5))
print(Solution().countBits(2))
