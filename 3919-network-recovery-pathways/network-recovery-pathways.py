from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        high = 0

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indeg[v] += 1
            high = max(high, cost)

        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []

        while q:
            u = q.popleft()
            order.append(u)

            for v, cost in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def possible(min_edge):
            dist = [10**20] * n
            dist[0] = 0

            for u in order:
                if dist[u] > k or not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost >= min_edge and online[v]:
                        dist[v] = min(dist[v], dist[u] + cost)

            return dist[n - 1] <= k

        ans = -1
        low = 0

        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans