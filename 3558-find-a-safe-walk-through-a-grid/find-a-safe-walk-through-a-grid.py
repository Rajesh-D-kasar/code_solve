class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        import heapq

        m, n = len(grid), len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]

        # Damage includes the starting cell if it is unsafe.
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            damage, r, c = heapq.heappop(heap)

            if damage != dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return damage < health

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_damage = damage + grid[nr][nc]

                    if new_damage < dist[nr][nc] and new_damage < health:
                        dist[nr][nc] = new_damage
                        heapq.heappush(heap, (new_damage, nr, nc))

        return False