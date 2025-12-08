class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        visited = set()
        num_copy = num

        while num_copy > 0:
            dig = num_copy % 10
            if num % dig == 0:
                count += 1
            num_copy //= 10

        return count

print(Solution().countDigits(999345561))
print(Solution().countDigits(121))
print(Solution().countDigits(7))
print(Solution().countDigits(1248))


