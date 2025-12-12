# class Solution:
#     def findComplement(self, num: int) -> int:
#         bit_num = bin(num)
#         complement = ''
#
#         for char in bit_num[2:]:
#             if char == '1':
#                 complement += '0'
#             else:
#                 complement += '1'
#
#         return int(complement, 2)

class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()

        dummy = (1 << bit_length) - 1

        return num ^ dummy

print(Solution().findComplement(5))
print(Solution().findComplement(1))