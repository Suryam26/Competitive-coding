def findFloor(root, key):
    floor = -1

    while root:
        if root.data == key:
            floor = root.data
            return floor

        if root.data > key:
            root = root.left
        else:
            floor = root.data
            root = root.right

    return floor
