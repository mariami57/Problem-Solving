from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image

        rows = len(image)
        cols = len(image[0])
        q = deque([(sr,sc)])
        image[sr][sc] = color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r,c = q.popleft()

            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start:
                    image[nr][nc] = color
                    q.append((nr,nc))

        return image

print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))