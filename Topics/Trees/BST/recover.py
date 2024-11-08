first = None
mid = None
prev = None
last = None


def inorder(root):
    global first, mid, prev, last
    if root:
        inorder(root.left)
        if prev and prev.val > root.val:
            if not first:
                first = prev
                mid = root
            else:
                last = root

    prev = root
    inorder(root.right)


def recoverTree(root):
    global first, mid, prev, last
    inorder(root)
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and mid:
        first.val, mid.val = mid.val, first.val
