from binarytree import Node


arr = []


def getPath(root, x):
    if not root:
        return False

    arr.append(root.data)
    if root.data == x:
        return True

    if getPath(root.left, x) or getPath(root.right, x):
        return True

    arr.pop()
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

getPath(root, 5)
print(arr)
