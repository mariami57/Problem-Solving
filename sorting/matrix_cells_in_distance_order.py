from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distances = {}

        for r in range(rows):
            for c in range(cols):
                distance = abs(r-rCenter) + abs(c-cCenter)
                if distance in distances:
                    distances[distance].append([r,c])
                else:
                    distances[distance] = [[r,c]]

        sorted_dict = sorted(distances.items(), key=lambda x: x[0])

        result = []
        for d, c in sorted_dict:
            result.extend(c)
        return result

print(Solution().allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2))
print(Solution().allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0))
print(Solution().allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1))

