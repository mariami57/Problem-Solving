class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        sp, tp = 0, 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)



print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))
