from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i = 0
        j = len(s)
        result = []

        for idx in range(len(s)):
            if s[idx] == 'D':
                result.append(j)
                j-=1
            else:
                result.append(i)
                i+=1
        return result + [i]


print(Solution().diStringMatch(s = "IDID"))
print(Solution().diStringMatch(s = "DDI"))
print(Solution().diStringMatch(s = "III"))
