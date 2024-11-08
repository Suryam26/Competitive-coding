class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def find_parent(self, node):
        """
        Time Complexity: O(4Alpha) ~ O(1)
        """
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        u_parent = self.find_parent(u)
        v_parent = self.find_parent(v)

        if u_parent == v_parent:
            return

        if self.size[u_parent] < self.size[v_parent]:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        else:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]

    def union_by_rank(self, u, v):
        u_parent = self.find_parent(u)
        v_parent = self.find_parent(v)

        if u_parent == v_parent:
            return

        if self.rank[u_parent] < self.rank[v_parent]:
            self.parent[u_parent] = v_parent
        elif self.rank[u_parent] > self.rank[v_parent]:
            self.parent[v_parent] = u_parent
        else:
            self.parent[v_parent] = u_parent
            self.rank[u_parent] += 1
