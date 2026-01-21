class Solution:
    def minimumChairs(self, s: str) -> int:
        curr, max_count = 0, 0

        for char in s:
            if char == 'E':
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr -= 1
        return max(max_count, curr)


print(Solution().minimumChairs("EEEEEEE"))
print(Solution().minimumChairs("ELELEEL"))
print(Solution().minimumChairs("ELEELEELLL"))
