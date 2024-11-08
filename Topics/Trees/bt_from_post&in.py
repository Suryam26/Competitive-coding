from binarytree import Node
# from dfs import postorder


def buildNode(postorder, postStart, postEnd, inorder, inStart, inEnd, inMap):
    if postStart > postEnd or inStart > inEnd:
        return None

    root = Node(postorder[postEnd])
    inRoot = inMap[root.data]
    leftSub = inRoot - inStart

    root.left = buildNode(postorder, postStart, postStart +
                          leftSub - 1, inorder, inStart, inRoot-1, inMap)
    root.right = buildNode(postorder, postStart+leftSub,
                           postEnd-1, inorder, inRoot+1, inEnd, inMap)

    return root


def buildTree(postorder, inorder):
    inMap = {}
    for i in range(len(inorder)):
        inMap[inorder[i]] = i

    root = buildNode(postorder, 0, len(postorder)-1,
                     inorder, 0, len(inorder)-1, inMap)
    return root


inorder = [9, 3, 15, 20, 7]
post = [9, 15, 7, 20, 3]

root = buildTree(post, inorder)
# print(postorder(root))
