class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_num = str(bin(n)[2:])

        return bit_num.count('1')

print(Solution().hammingWeight(11))
print(Solution().hammingWeight(128))
print(Solution().hammingWeight(2147483645))
