# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         if n == 1:
#             return n
#         for i in range(1, n+1):
#             n-=i
#
#             if n < 0:
#                 return i - 1



class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1,n
        while left <= right:
            mid = (right + left) // 2
            num = (mid/2) * (mid+1)
            if num <=n:
                left=mid+1
            else:
                right=mid-1
        return right



print(Solution().arrangeCoins(5))