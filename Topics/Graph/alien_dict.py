def find_order(alien_dict, k):
    n = len(alien_dict)

    adj = [[] for _ in range(k)]
    for i in range(1, n):
        s1, s2 = alien_dict[i - 1], alien_dict[i]
        n, m = len(s1), len(s2)

        u, v = 0, 0
        while u < n and v < m:
            if s1[u] != s2[v]:
                adj[ord(s1[u]) - ord('a')].append(ord(s2[v]) - ord('a'))
                break

            u += 1
            v += 1

    in_degree = [0] * k
    for i in range(k):
        for adj_node in adj[i]:
            in_degree[adj_node] += 1

    queue = []
    for i in range(k):
        if in_degree[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(chr(ord('a') + node))

        for adj_node in adj[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                queue.append(adj_node)

    return "".join(ans)
