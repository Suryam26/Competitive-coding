from binarytree import Node


def preorder(root):
    stack = [root]

    while(len(stack)):
        node = stack.pop()
        print(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Pre-order: ")
preorder(root)
