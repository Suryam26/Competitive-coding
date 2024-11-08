def validate(root, leftR, rightR):
    if not root:
        return True

    if root.data <= leftR or root.data >= rightR:
        return False

    return validate(root.left, leftR, root.data) and validate(root.right, root.data, rightR)


def isValidBST(root):
    return validate(root, float('-inf'), float('inf'))
