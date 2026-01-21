class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        total_sum = 1

        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                total_sum += i
                if i != num // i:
                    total_sum += num // i

        return total_sum == num

print(Solution().checkPerfectNumber(28))
print(Solution().checkPerfectNumber(7))
