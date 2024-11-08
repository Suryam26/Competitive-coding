class Node:
    def __init__(self):
        self.children = [None] * 2


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = Node()
            node = node.children[bit]

    def maxXOR(self, num):
        maxNum = 0
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.children[1-bit]:
                maxNum = maxNum | (1 << i)
                node = node.children[1-bit]
            else:
                node = node.children[bit]

        return maxNum


def maxXOR(n, m, arr1, arr2):
    t = Trie()

    for i in arr1:
        t.insert(i)

    ans = 0
    for j in arr2:
        ans = max(ans, t.maxXOR(j))

    return ans


arr1 = [6, 6, 0, 6, 8, 5, 6]
arr2 = [1, 7, 1, 7, 8, 0, 2]
n, m = len(arr1), len(arr2)

print(maxXOR(n, m, arr1, arr2))
