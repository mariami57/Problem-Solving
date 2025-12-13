class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''

        if num == 0:
            return '0'

        n = abs(num)

        while n != 0:
            rem = n % 7
            res += str(rem)
            n //= 7

        if num < 0:
            return '-'+res[::-1]
        else:
            return res[::-1]

print(Solution().convertToBase7(-12))
print(Solution().convertToBase7(100))

