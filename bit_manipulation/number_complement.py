class Solution:
    def findComplement(self, num: int) -> int:
        bit_num = bin(num)
        complement = ''

        for char in bit_num[2:]:
            if char == '1':
                complement += '0'
            else:
                complement += '1'

        return int(complement, 2)

print(Solution().findComplement(5))
print(Solution().findComplement(1))