class DLL:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {}
        self.capacity = capacity

    def delete_node(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add_node(self, node):
        p = self.head
        n = self.head.next
        node.next = n
        node.prev = p
        p.next = node
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.delete_node(node)
            self.add_node(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.delete_node(node)
            self.add_node(node)
            node.value = value
            return

        node = DLL(key, value)
        if self.capacity == 0:
            d_node = self.tail.prev
            self.delete_node(d_node)
            self.hashmap.pop(d_node.key, None)
        else:
            self.capacity -= 1

        self.add_node(node)
        self.hashmap[key] = node
        return
