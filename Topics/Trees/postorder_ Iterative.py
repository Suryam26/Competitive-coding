from binarytree import Node


def postorder_1(root):
    '''
    Using 2 Stacks
    '''
    ans = []
    stack = [root]

    while(len(stack)):
        node = stack.pop()
        ans.append(node)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    while(len(ans)):
        node = ans.pop()
        print(node.data)


def postorder_2(root):
    '''
    Using 1 Stack
    '''
    stack = []

    node = root
    while(node or len(stack)):
        if node:
            stack.append(node)
            node = node.left
        else:
            temp = stack[-1].right
            if temp:
                node = temp
            else:
                temp = stack.pop()
                print(temp.data)
                while len(stack) and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Post-order-1: ")
postorder_1(root)

print("Post-order-2: ")
postorder_2(root)
