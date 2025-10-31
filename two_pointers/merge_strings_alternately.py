class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = []


        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i+=1


        result.append(word2[len(word1):])
        result.append(word1[len(word2):])


        return ''.join(result)

print(Solution().mergeAlternately(word1 = "abcd", word2 = "pq"))
