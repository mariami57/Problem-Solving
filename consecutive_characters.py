class Solution:
    def maxPower(self, s: str) -> int:
        power_count, curr_count = 1, 1

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curr_count += 1
            else:
                power_count = max(power_count, curr_count)
                curr_count = 1

        return max(power_count, curr_count)

print(Solution().maxPower("leetcode"))
print(Solution().maxPower("abbcccddddeeeeedcba"))