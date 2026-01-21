class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ''

        if num == 0:
            return '0'

        n = abs(num)

        while n != 0:
            rem = n % 7
            result += str(rem)

            n //= 7

        if num < 0:
            return '-' + result[::-1]
        else:
            return result[::-1]

print(Solution().convertToBase7(-7))
print(Solution().convertToBase7(100))

