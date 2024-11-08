from binarytree import Node


def bfs(root):
    if root:
        queue = []
        queue.append(root)

        while(len(queue)):
            node = queue.pop(0)
            print(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order: ")
bfs(root)
