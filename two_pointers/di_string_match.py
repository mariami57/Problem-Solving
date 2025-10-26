from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        low, high = 0, len(s)
        for x in s:
            if x=='I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        return result+[low]

print(Solution().diStringMatch(s = "IDID"))
print(Solution().diStringMatch(s = "DDI"))
print(Solution().diStringMatch(s = "III"))
