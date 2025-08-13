class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in substring:
                substring.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
                substring.add(s[right])

        return max_length

s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))