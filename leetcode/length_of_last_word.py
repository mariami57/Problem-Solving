class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n_list = s.strip().split(' ')

        return len(n_list[-1])

print(Solution().lengthOfLastWord('luffy is still joyboy'))