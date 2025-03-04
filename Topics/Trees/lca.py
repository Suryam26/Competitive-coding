def lowest_common_ancestor(root, p, q):
    if root:
        if root == p or root == q:
            return root

        left = lowest_common_ancestor(root.left, p, q)
        right = lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root

        return left or right
