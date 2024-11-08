from binarytree import Node


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder: ")
inorder(root)

print("\nPre-order: ")
preorder(root)

print("\nPost-order: ")
postorder(root)
