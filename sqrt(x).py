class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        mid = 0
        y = 1
        target = x
        while y <= target:
            mid = (y+target) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                y = mid + 1
            else:
                target = mid - 1
        return target


print(Solution().mySqrt(8))
