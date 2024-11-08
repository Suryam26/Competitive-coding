def findRight(root):
    if not root.right:
        return root
    return findRight(root.right)


def delete(root):
    if not root.left:
        return root.right
    if not root.right:
        return root.left

    right = root.right
    lastRight = findRight(root.left)
    lastRight.right = right

    return root.left


def deleteNode(root, key):
    if not root:
        return None

    if root.val == key:
        return delete(root)

    result = root
    while root:
        if root.val > key:
            if root.left and root.left.val == key:
                root.left = delete(root.left)
                break
            else:
                root = root.left
        else:
            if root.right and root.right.val == key:
                root.right = delete(root.right)
                break
            else:
                root = root.right

    return result
