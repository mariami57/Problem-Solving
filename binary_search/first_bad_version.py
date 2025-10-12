BAD_VERSION = 2

def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        mid = 0

        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start



solution = Solution().firstBadVersion(3)
print(solution)