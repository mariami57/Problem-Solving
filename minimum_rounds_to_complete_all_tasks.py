from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq = Counter(tasks)
        ans = 0
        for c in freq.values():
            if c == 1:
                return -1
            ans += (c+2) // 3
        return ans

print(Solution().minimumRounds([2,2,3,3,2,4,4,4,4,4]))