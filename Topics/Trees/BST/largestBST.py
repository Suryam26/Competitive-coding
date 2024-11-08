class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize


def largestBST(root):
    if not root:
        return NodeValue(float('inf'), float('-inf'), 0)

    left = largestBST(root.left)
    right = largestBST(root.right)

    if left.maxNode < root.data and root.data < right.minNode:
        return NodeValue(min(left.minNode, root.data), max(root.data, right.maxNode), left.maxSize + right.maxSize + 1)

    return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(8)
root.right.right = Node(7)

print(largestBST(root).maxSize)
