result = []

def search(node):
    if node:
        search(node.left)
        result.append(node.val)
        search(node.right)


def k_smallest(root, k):
    search(root)
    return result[k-1]


