from typing import List


# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         result = []
#         flag = False
#
#         for i in range(left, right + 1):
#             temp = i
#             while temp > 0:
#                 dig = temp % 10
#                 if dig == 0 or i % dig != 0:
#                     flag = True
#                     break
#                 temp //= 10
#             if not flag:
#                 result.append(i)
#             else:
#                 flag = False
#
#         return result

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []


        for i in range(left, right + 1):
            temp = i
            while temp > 0:
                dig = temp % 10
                if dig == 0 or i % dig != 0:
                    break
                temp //= 10
            if temp == 0:
                result.append(i)


        return result

print(Solution().selfDividingNumbers(left = 1, right = 22))
print(Solution().selfDividingNumbers(left = 47, right = 85))

