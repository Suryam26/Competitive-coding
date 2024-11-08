from binarytree import Node as TreeNode

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    cur = root
    prev = None
    while cur:
        prev = cur
        if cur.data > val:
            cur = cur.left
        else:
            cur = cur.right

    if prev.data > val:
        prev.left = TreeNode(val)
    else:
        prev.right = TreeNode(val)

    return root
