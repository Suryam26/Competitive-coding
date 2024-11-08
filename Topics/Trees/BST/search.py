def searchBST(root, val):
    while root and root.data != val:
        root = root.left if val < root.data else root.right

    return root
