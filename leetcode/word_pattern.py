class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapped = {}

        s = s.split()

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if s[i] in mapped.values() and pattern[i] not in mapped:
                return False
            if pattern[i] in mapped and  s[i] != mapped[pattern[i]]:
                    return False
            else:
                mapped[pattern[i]] = s[i]

        return True

print(Solution().wordPattern(pattern = "abba", s = "dog dog dog dog"))
print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(Solution().wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
