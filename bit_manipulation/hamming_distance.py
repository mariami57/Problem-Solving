class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

print(Solution().hammingDistance(x = 1, y = 4))
print(Solution().hammingDistance(x = 3, y = 1))