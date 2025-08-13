BAD_VERSION = 4

def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_v = 1
        last_v = n

        while first_v < last_v:
            mid = first_v + (last_v - first_v) // 2
            if isBadVersion(mid):
                last_v = mid
            else:
                first_v = mid + 1
        return first_v



solution = Solution().firstBadVersion(6)
print(solution)