class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_length = 0
        for i in  range(len(s)):
            if s[i] not in substring:
                substring.add(s[i])
            else:
                if max_length < len(substring):
                    max_length = len(substring)
                    substring = set()
                    substring.add(s[i])


        return max_length

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))