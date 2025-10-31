class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ''

        if ch not in word:
            return ''.join(word)
        else:
            idx = word.index(ch)
            reversed = word[:idx+1][::-1]
            result+= reversed
            result+= word[idx+1:]

            return result

print(Solution().reversePrefix(word = "abcd", ch = "z"))