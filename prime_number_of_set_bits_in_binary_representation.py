import math


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n <= 1:
                return False

            if n <= 3:
                return True

            if n % 2 == 0 or n % 3 == 0:
                return False

            i = 5

            while i * i <= n:
                if n % i == 0 or n %(i+2) == 0:
                    return False
                i+=6
            return True

        c = 0

        for i in range(left, right + 1):
            val = bin(i).count('1')
            if isPrime(val):
                c += 1
        return c


print(Solution().countPrimeSetBits(left = 10, right = 15))
print(Solution().countPrimeSetBits(left = 6, right = 10))


