class Bridges:
    """
    Tarjan's algorithm for finding bridges in a graph.
    Time Complexity: O(V+2E)
    Space Complexity: O(3V)
    """
    time = 1

    def dfs(self, node, parent, visited, tin, low, bridges, adj):
        self.time += 1
        visited[node] = True

        tin[node] = low[node] = self.time
        for neighbour in adj[node]:
            if neighbour != parent:
                if not visited[neighbour]:
                    self.dfs(neighbour, node, visited, tin, low, bridges, adj)

                    low[node] = min(low[node], low[neighbour])
                    if low[neighbour] > tin[node]:
                        bridges.append([node, neighbour])

                else:
                    low[node] = min(low[node], low[neighbour])

    def find_bridges(self, n: int, connections):
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        tin, low = [float('inf')] * n, [float('inf')] * n

        bridges = []
        for node in range(n):
            if not visited[node]:
                self.dfs(node, -1, visited, tin, low, bridges, adj)

        return bridges
