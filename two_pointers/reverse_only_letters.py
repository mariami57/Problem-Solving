class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
            if not s[j].isalpha():
                j-=1
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)

print(Solution().reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))
