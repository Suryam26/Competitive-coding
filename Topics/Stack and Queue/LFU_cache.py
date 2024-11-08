class DLL:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.next = None
        self.prev = None


class LRU:
    size = 0
    head = DLL(-1, -1)
    tail = DLL(-1, -1)
    head.next = tail
    tail.prev = head

    def is_empty(self):
        return self.size == 0

    def add_node(self, node):
        self.size += 1
        p = self.head
        n = self.head.next
        node.prev = p
        node.next = n
        p.next = node
        n.prev = node

    def delete_node(self, node):
        self.size -= 1
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = capacity
        self.min_freq = 1
        self.key_node = {}
        self.freq_list = {}

    def update_freq_list(self, node):
        freq = node.count
        prev_list = self.freq_list[freq]
        prev_list.delete_node(node)

        new_freq = freq + 1
        if new_freq not in self.freq_list:
            self.freq_list[new_freq] = LRU()

        new_list = self.freq_list[new_freq]
        new_list.add_node(node)
        node.count = new_freq

        if self.min_freq == freq and prev_list.is_empty():
            self.min_freq = new_freq

    def get(self, key: int) -> int:
        if key in self.key_node:
            node = self.key_node[key]
            self.update_freq_list(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self.update_freq_list(node)
            return

        if self.size == 0:
            min_freq_list = self.freq_list[self.min_freq]
            node = min_freq_list.tail.prev
            self.key_node.pop(node.key, None)
            min_freq_list.delete_node(node)
        else:
            self.size -= 1

        self.min_freq = 1
        new_node = DLL(key, value)
        self.key_node[key] = new_node

        if self.min_freq not in self.freq_list:
            self.freq_list[self.min_freq] = LRU()

        min_freq_list = self.freq_list[self.min_freq]
        min_freq_list.add_node(new_node)
