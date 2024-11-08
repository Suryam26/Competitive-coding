def parentTracker(root):
    parent = {root: None}
    q = [root]
    while len(q):
        node = q.pop(0)

        if node.left:
            parent[node.left] = node
            q.append(node.left)

        if node.right:
            parent[node.right] = node
            q.append(node.right)

    return parent


def distanceK(root, target, k):
    if k == 0:
        return [target.val]

    parent = parentTracker(root)

    q = [target]
    visited = {target}
    
    dist = 0
    while len(q):
        if dist == k:
            break

        dist += 1
        for i in range(len(q)):
            node = q.pop(0)

            if node.left and node.left not in visited:
                visited.add(node.left)
                q.append(node.left)

            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append(node.right)

            if parent[node] and parent[node] not in visited:
                visited.add(parent[node])
                q.append(parent[node])

    result = []
    while(len(q)):
        result.append(q.pop(0).val)

    return result
