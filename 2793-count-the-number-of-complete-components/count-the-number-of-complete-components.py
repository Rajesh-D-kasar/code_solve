class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        complete_components = 0

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True

            nodes = 0
            total_degree = 0

            while stack:
                node = stack.pop()

                nodes += 1
                total_degree += len(graph[node])

                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        stack.append(neighbour)

            # Complete component me each node ke paas nodes - 1 edges hongi
            if total_degree == nodes * (nodes - 1):
                complete_components += 1

        return complete_components