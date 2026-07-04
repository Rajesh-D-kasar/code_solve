class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for city1, city2, distance in roads:
            graph[city1].append((city2, distance))
            graph[city2].append((city1, distance))

        visited = set()
        stack = [1]
        visited.add(1)

        min_score = float("inf")

        while stack:
            city = stack.pop()

            for neighbour, distance in graph[city]:
                min_score = min(min_score, distance)

                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return min_score