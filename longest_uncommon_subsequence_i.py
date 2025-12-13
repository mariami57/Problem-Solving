class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        return  max(len(a), len(b))

print(Solution().findLUSlength(a = "aaa", b = "aaa"))
print(Solution().findLUSlength(a = "aba", b = "cdc"))
print(Solution().findLUSlength(a = "aaa", b = "bbb"))
print(Solution().findLUSlength(a = "aefawfawfawfaw", b = "aefawfeawfwafwaef"))

