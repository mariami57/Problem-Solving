# class Solution:
#     def kthCharacter(self, k: int) -> str:
#
#         def recurse(word):
#             if k == 1:
#                 return 'a'
#             if len(word) >= k:
#                 return word[k-1]
#
#             new_word = word
#             for ch in word:
#                 new_word += chr(ord(ch) + 1)
#
#             return recurse(new_word)
#     return recurse('a')


class Solution:
    def kthCharacter(self, k: int) -> str:


        def helper(k):
            if k == 1:
                return 'a'

            length = 1

            while length * 2 < k:
                length *= 2

            if k <= length:
                return helper(k)

            return chr(ord(helper(k - length)) + 1)
        return helper(k)


print(Solution().kthCharacter(10))


