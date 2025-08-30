class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     str_x = str(x)
    #     reversed_x = str_x[::-1]
    #     if str_x == reversed_x:
    #         return True
    #     else:
    #         return False

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_number = 0
        while reverse_number < x:
            reverse_number = reverse_number * 10 + x % 10
            x = x // 10

        return reverse_number == x or x == reverse_number // 10


print(Solution().isPalindrome(121))
