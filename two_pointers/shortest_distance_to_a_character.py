from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = ['*'] * len(s)
        i, j = 0, 0

        while i < len(s) and j < len(s):
            if s[i] == s[j] == c:
                answer[i] = 0
                i += 1
                j += 1
            elif s[i] != c and s[j] == c:
                answer[i] = abs(i-j)
                i+=1
            elif s[i] != c and s[j] != c:
                j += 1

        i = j = len(s) - 1
        while i >= 0 and j >= 0:
            if s[i] == s[j] == c:
                answer[i] = 0
                i -= 1
                j -= 1
            elif s[i] != c and s[j] == c:
                if type(answer[i]) == int:
                    answer[i] = min(answer[i], abs(i-j))
                else:
                    answer[i] = abs(i-j)
                i -= 1
            elif s[i] != c and s[j] != c:
                j -= 1


        return answer

print(Solution().shortestToChar(s = "loveleetcode", c = "e"))