from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        limit = len(flowerbed)

        while i < limit:
            if n == 0:
                return True

            if flowerbed[i] == 0:
                if i+1 >= limit or flowerbed[i+1] == 0:
                    n -= 1
                else:
                    i+= 1
            i += 2

        return n == 0


print(Solution().canPlaceFlowers(flowerbed = [0], n = 1))
print(Solution().canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1))
print(Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
