from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_order = {}

        for i, letter in enumerate(order):
            letter_order[letter] = i

        for i in range(1, len(words)):
            p = 0
            word1 = words[i-1]
            word2 = words[i]

            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False

            while p < len(word1):
                if letter_order[word1[p]] < letter_order[word2[p]]:
                    break
                elif word1[p] == word2[p]:
                    p += 1
                else:
                    return False

            continue
        return True

print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))


