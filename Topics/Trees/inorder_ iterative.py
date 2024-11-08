from binarytree import Node


def inorder(root):
    stack = []

    node = root
    while(True):
        if node:
            stack.append(node)
            node = node.left
        else:
            if not len(stack):
                break
            node = stack.pop()
            print(node.data)
            node = node.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder: ")
inorder(root)
