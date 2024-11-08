class ArticulationPoint:
    """
    Time Complexity: O(V+2E)
    Space Complexity: O(4V)
    """
    time = 0

    def dfs(self, node, parent, visited, tin, low, marked, adj):
        self.time += 1

        visited[node] = True
        tin[node] = low[node] = self.time

        child = 0
        for neighbour in adj[node]:
            if neighbour != parent:
                if not visited[neighbour]:
                    child += 1

                    self.dfs(neighbour, node, visited, tin, low, marked, adj)

                    low[node] = min(low[node], low[neighbour])
                    if low[neighbour] >= tin[node] and parent != -1:
                        marked[node] = True

                else:
                    low[node] = min(low[node], tin[neighbour])

        if child > 1 and parent == -1:
            marked[node] = True

    def articulation_points(self, n, adj):
        visited = [False] * n
        tin, low = [float('inf')] * n, [float('inf')] * n

        marked = [False] * n
        for node in range(n):
            if not visited[node]:
                self.dfs(node, -1, visited, tin, low, marked, adj)

        ans = []
        for i in range(n):
            if marked[i]:
                ans.append(i)

        if ans:
            return ans

        return [-1]


a = ArticulationPoint()
print(a.articulation_points(4, [[1], [0, 2, 3], [1], [1]]))
