from typing import List


class Solution:
    # def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    #     for i in range(len(image)):
    #         image[i] = [ 1 - x for x in image[i][::-1]]
    #     return image

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left = 0
            right = len(row) - 1

            while left <= right:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1

                left += 1
                right -= 1
        return image


print(Solution().flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))