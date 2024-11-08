from trie import Node


class Trie:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def _char_to_index(ch):
        return ord(ch)-ord('a')

    def insert(self, key):
        node = self.root
        for i in key:
            index = self._char_to_index(i)

            if not node.children[index]:
                node.children[index] = Node()

            node = node.children[index]

        node.isEndOfWord = True

    def search(self, key):
        node = self.root
        for i in key:
            index = self._char_to_index(i)

            if not node.children[index]:
                return False

            node = node.children[index]

        return node.isEndOfWord
