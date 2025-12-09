class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        used = []

        for char in ransomNote:
            if ransomNote.count(char) > magazine.count(char):
                return False
            if char not in magazine:
                return False
            used.append(char)


        return True


print(Solution().canConstruct(ransomNote = "fffbfg", magazine = "effjfggbffjdgbjjhhdegh"))
print(Solution().canConstruct(ransomNote = "a", magazine = "b"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))
