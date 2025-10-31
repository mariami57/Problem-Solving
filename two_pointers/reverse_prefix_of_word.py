# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         result = ''
#
#         if ch not in word:
#             return word
#         else:
#             idx = word.index(ch)
#             result+= word[:idx+1][::-1]
#             result+= word[idx+1:]
#
#             return result
#
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            result = []
            word = list(word)

            for i in range(len(word)):
                if word[i] == ch:
                    l, r = 0, i
                    while l < r:
                        word[l], word[r] = word[r], word[l]
                        l += 1
                        r -= 1
                    return ''.join(word)

print(Solution().reversePrefix(word = "abcdefd", ch = "d"))
print(Solution().reversePrefix(word = "abcd", ch = "z"))