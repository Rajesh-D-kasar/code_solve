from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS from all thieves.
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Max-heap path search.
        # We want the path whose minimum distance-to-thief is as large as possible.
        heap = [(-dist[0][0], 0, 0)]
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True

        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    seen[nr][nc] = True
                    new_safe = min(safe, dist[nr][nc])
                    heapq.heappush(heap, (-new_safe, nr, nc))

        return 0