class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        new_s = []

        for word in s:
           new_s.append(word[::-1])

        return ' '.join(new_s)

print(Solution().reverseWords(s = "Let's take LeetCode contest"))
