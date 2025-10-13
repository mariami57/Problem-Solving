# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         if num % 9 == 0:
#             return 9
#         else:
#             return (num % 9)


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return self.addDigits(sum)

print(Solution().addDigits(38))
