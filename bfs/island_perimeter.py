from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return self.bfs(grid, row, col, visited)

    def bfs(self, grid, sr, sc, visited):

        rows = len(grid)
        cols = len(grid[0])
        q = deque([(sr,sc)])
        visited.add((sr,sc))
        perimeter = 0

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c+dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    perimeter += 1

                elif grid[nr][nc] == 0:
                    perimeter += 1

                elif (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))

        return perimeter



