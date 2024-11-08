from binarytree import Node


def morrisTraversal(root):
    result = []

    curr = root
    while curr:
        if not curr.left:
            result.append(curr.data)
            curr = curr.right
        else:
            prev = curr.left

            while prev.right and prev.right != curr:
                prev = prev.right

            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                result.append(curr.data)
                curr = curr.right

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(morrisTraversal(root))
