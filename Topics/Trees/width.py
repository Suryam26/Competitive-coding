from binarytree import Node


def maxWidth(root):
    if not root:
        return 0

    width = 0
    queue = [(root, 0)]

    while len(queue):
        _, right = queue[-1]
        _, left = queue[0]

        width = max(width, right-left+1)

        for i in range(len(queue)):
            node, index = queue.pop(0)
            index -= left

            if node.left:
                queue.append((node.left, 2*index+1))

            if node.right:
                queue.append((node.right, 2*index+2))

    return width


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(maxWidth(root))
