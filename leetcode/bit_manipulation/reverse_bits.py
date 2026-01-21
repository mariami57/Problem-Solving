class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, '032b')
        reversed_bits = bits[::-1]

        return int(reversed_bits, 2)

print(Solution().reverseBits(43261596))