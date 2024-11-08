from binarytree import Node as TreeNode


i = 0


def built(arr, upper):
    global i
    if len(arr) == i or arr[i] > upper:
        return None

    node = TreeNode(arr[i])
    i += 1
    node.left = built(arr, node.data)
    node.right = built(arr, upper)

    return node


preorder = [8, 5, 1, 7, 10, 12]
print(built(preorder, float('inf')))
