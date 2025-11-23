class Solution:
    def kthCharacter(self, k: int) -> str:

        def recurse(word):
            if k == 1:
                return 'a'
            if len(word) >= k:
                return word[k-1]

            new_word = word
            for ch in word:
                new_word += chr(ord(ch) + 1)

            return recurse(new_word)


        return recurse('a')
print(Solution().kthCharacter(5))


