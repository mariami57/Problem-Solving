class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        start  = 0
        end = 0
        substring = ''

        while len(substring) < len(s) // 2:
            substring = s[start:end+1]
            repetition = len(s) // len(substring)
            if substring * repetition == s:
                return True
            end += 1
        return False




print(Solution().repeatedSubstringPattern(s = "aba"))
print(Solution().repeatedSubstringPattern(s = "abac"))
print(Solution().repeatedSubstringPattern(s = "abab"))
print(Solution().repeatedSubstringPattern(s = "abcabcabcabc"))