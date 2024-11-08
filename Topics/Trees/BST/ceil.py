def findCeil(root, key):
    ceil = -1

    while root:
        if root.data == key:
            ceil = root.data
            return ceil

        if root.data < key:
            root = root.right
        else:
            ceil = root.data
            root = root.left

    return ceil
