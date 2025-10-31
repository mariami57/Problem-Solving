class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ''

        if ch not in word:
            return word
        else:
            idx = word.index(ch)
            result+= word[:idx+1][::-1]
            result+= word[idx+1:]

            return result


print(Solution().reversePrefix(word = "abcd", ch = "z"))