from binarytree import Node


def isLeaf(root):
    if not root.left and not root.right:
        return True
    return False


def leftBoundary(root):
    ans = []
    cur = root.left
    while cur:
        if not isLeaf(cur):
            ans.append(cur.data)

        if cur.left:
            cur = cur.left
        else:
            cur = cur.right

    return ans


def rightBoundary(root):
    ans = []
    cur = root.right
    while cur:
        if not isLeaf(cur):
            ans.append(cur.data)

        if cur.right:
            cur = cur.right
        else:
            cur = cur.left

    return ans


def addLeaves(root, ans):
    if isLeaf(root):
        ans.append(root.data)

    if root.left:
        addLeaves(root.left, ans)
    if root.right:
        addLeaves(root.right, ans)


def antiClockBoundary(root):
    result = []

    if root:
        result.append(root.data)

    result += leftBoundary(root)
    addLeaves(root, result)
    result += rightBoundary(root)[::-1]

    return result


def clockBoundary(root):
    result = []

    if root:
        result.append(root.data)

    result += rightBoundary(root)
    temp = []
    addLeaves(root, temp)
    result += temp[::-1]
    result += leftBoundary(root)[::-1]

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Anti-Clock:", *antiClockBoundary(root))
print("Clock:", *clockBoundary(root))
