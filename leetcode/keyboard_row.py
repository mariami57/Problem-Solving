from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = 'qwertyuiop'
        r2 = 'asdfghjkl'
        r3 = 'zxcvbnm'

        result = []

        for word in words:
            w = word.lower()
            if len(set(r1 + w)) == len(r1) or len(set(r2 + w)) == len(r2) or len(set(r2+w))== len(r3):
                result.append(word)
        return result

print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))


