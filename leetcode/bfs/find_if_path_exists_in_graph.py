from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        q = deque([source])

        visited.add(source)

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)

        return False

