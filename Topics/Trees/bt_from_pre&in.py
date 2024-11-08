from binarytree import Node
# from dfs import preorder


def buildNode(preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
    if preStart > preEnd or inStart > inEnd:
        return None

    root = Node(preorder[preStart])
    inRoot = inMap[root.data]
    leftSub = inRoot - inStart

    root.left = buildNode(preorder, preStart+1, preStart +
                          leftSub, inorder, inStart, inRoot-1, inMap)
    root.right = buildNode(preorder, preStart+leftSub+1,
                           preEnd, inorder, inRoot+1, inEnd, inMap)

    return root


def buildTree(preorder, inorder):
    inMap = {}
    for i in range(len(inorder)):
        inMap[inorder[i]] = i

    root = buildNode(preorder, 0, len(preorder)-1,
                     inorder, 0, len(inorder)-1, inMap)
    return root


pre = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(pre, inorder)
# print(preorder(root))
