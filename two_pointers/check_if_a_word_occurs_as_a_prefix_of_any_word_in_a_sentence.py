# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         words = sentence.split()
#         for i,word in enumerate(words):
#             if word.startswith(searchWord):
#                 return i+1
#         return -1


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for idx, word in enumerate(words):
            for i in range(len(word)):
                if word[i] == searchWord[i]:
                    i += 1
                    if i == len(searchWord):
                        return idx + 1
                else:
                    break

        return -1



print(Solution().isPrefixOfWord(sentence = "b bu bur burg burger", searchWord = "burg"))