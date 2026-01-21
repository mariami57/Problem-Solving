class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_num = bin(n)[2:]

        for i in range(1, len(bin_num)):
            if bin_num[i-1] == bin_num[i]:
                return False

        return True

print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(7))
print(Solution().hasAlternatingBits(11))