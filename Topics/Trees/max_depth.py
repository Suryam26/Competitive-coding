from binarytree import Node


def maxDepth(root):
    if not root:
        return 0

    lh = maxDepth(root.left)
    rh = maxDepth(root.right)

    return 1 + max(lh, rh)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(maxDepth(root))
