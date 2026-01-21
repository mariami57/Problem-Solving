class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for chr in s:
            num += str(ord(chr) - 97 + 1)
        num = int(num)
        sum = 0

        while k > 0:
            sum = 0
            while num > 0:
                dig = num % 10
                sum += dig
                num //= 10
            num = sum
            k -= 1
        return sum
    
print(Solution().getLucky(s = "iiii", k = 1))
print(Solution().getLucky(s = "zbax", k = 2))
print(Solution().getLucky(s = "leetcode", k = 2))