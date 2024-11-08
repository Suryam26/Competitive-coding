from binarytree import Node
# from dfs import inorder

def morrisFlatten(root):
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right:
                prev = prev.right

            prev.right = cur.right
            cur.right = cur.left
            cur.left = None

        cur = cur.right



prev = None
def flatten(root):
    global prev
    if not root:
        return

    flatten(root.right)
    flatten(root.left)

    root.right = prev
    root.left = None
    prev = root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

flatten(root)
# inorder(root)