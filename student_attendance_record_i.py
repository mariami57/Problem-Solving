class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') < 2 and 'LLL' not in s:
            return True
        return False

print(Solution().checkRecord("PPALLP"))
print(Solution().checkRecord("PPLLLL"))