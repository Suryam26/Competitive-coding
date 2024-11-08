class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0
        self.capacity = 0
        self.overflow = "Overflow: queue is full"
        self.underflow = "Underflow: queue is empty"

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    def push(self, element):
        if self.capacity == self.size:
            print(self.overflow)
            return
        self.queue[self.rear % self.size] = element
        self.rear += 1
        self.capacity += 1
        # print("Element added:", element)

    def pop(self):
        if self.is_empty():
            print(self.underflow)
            return -1
        temp = self.queue[self.front % self.size]
        self.queue[self.front % self.size] = None
        self.front += 1
        self.capacity -= 1
        return temp

    def print_queue(self):
        for i in range(self.front, self.rear):
            print(self.queue[i % self.size], end=" ")
        print()


# q = Queue(5)
# q.pop()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# q.push(6)
# q.print_queue()
# q.pop()
# q.pop()
# q.pop()
# q.print_queue()
