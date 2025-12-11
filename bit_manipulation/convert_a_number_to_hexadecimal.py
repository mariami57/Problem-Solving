# class Solution:
#     def toHex(self, num: int) -> str:
#         if num == 0:
#             return '0'
#
#         if num < 0:
#             num = ( 1 << 32) + num
#
#         hex_digits ='0123456789abcdef'
#         hex_num = ''
#
#         while num > 0:
#             digit = num % 16
#             hex_digit = hex_digits[digit]
#             hex_num = hex_digit + hex_num
#             num //= 16
#
#         return hex_num


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        res = ''

        if num < 0:
            num = ( 1 << 32) + num

        hex_digits= '0123456789abcdef'

        while num > 0:
            digit = num % 16
            hex_digit = hex_digits[digit]
            res = hex_digit + res
            num //= 16

        return res


print(Solution().toHex(-1))
print(Solution().toHex(26))
