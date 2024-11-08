from queue import Queue


class Stack:
    def __init__(self, size):
        self.queue = Queue(size)
        self.overflow = "Overflow: stack is full"
        self.underflow = "Underflow: stack is empty"

    def get_top(self):
        if self.queue.is_empty():
            print(self.underflow)
        return self.queue.front

    def push(self, element):
        if self.queue.capacity == self.queue.size:
            print(self.overflow)
            return

        self.queue.push(element)
        for i in range(self.queue.capacity-1):
            temp = self.queue.pop()
            self.queue.push(temp)
        print("Element added:", element)

    def pop(self):
        if self.queue.is_empty():
            print(self.underflow)
            return
        return self.queue.pop()

    def print_stack(self):
        self.queue.print_queue()


s = Stack(5)
s.pop()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.push(8)
s.print_stack()
s.pop()
s.pop()
s.pop()
s.pop()
s.print_stack()
