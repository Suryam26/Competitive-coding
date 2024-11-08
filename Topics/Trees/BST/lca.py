def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)

    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)

    return root
