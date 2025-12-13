from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []

        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 ="zxcvbnm"

        for word in words:
            w = word.lower()
            if len(set(l1+w)) == len(l1) or len(set(l2+w)) == len(l2) or len(set(l3+w)) == len(l3):
                result.append(word)

        return result

print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))


