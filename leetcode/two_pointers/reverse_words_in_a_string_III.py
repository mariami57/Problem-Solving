class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        new_s = []

        for word in s:
           new_s.append(word[::-1])

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         word = []
#
#         start = 0
#         end = 0
#
#         while end < len(s):
#             if s[end] == ' ':
#                 word.append(s[start:end][::-1])
#                 start = end + 1
#             if end == len(s)-1:
#                 word.append(s[start:end+1][::-1])
#                 start = end + 1
#             end+=1
#         return ' '.join(word)




print(Solution().reverseWords(s = "Let's take LeetCode contest"))
