class Solution:
    def repeatedCharacter(self, s: str) -> str:
        reps = set()
        for char in s:
            if char in reps:
                return char
            else:
                reps.add(char)

s = "abcdd"
sol = Solution().repeatedCharacter(s)
print(sol)