def inorderSuccessor(root, p):
    successor = None

    while root:
        if p.data >= root.data:
            root = root.right 

        else:
            successor = root
            root = root.left

    return successor