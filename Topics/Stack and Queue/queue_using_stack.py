from stack import Stack


class Queue:
    def __init__(self, size):
        self.input = Stack(size)
        self.output = Stack(size)
        self.overflow = "Overflow: queue is full"
        self.underflow = "Underflow: queue is empty"

    def push(self, element):
        if self.input.size == self.input.top + self.output.top + 2:
            print(self.overflow)
            return
        self.input.push(element)
        print("Element added:", element)

    def pop(self):
        if self.output.top == -1:
            for i in range(self.input.top+1):
                temp = self.input.pop()
                self.output.push(temp)

        return self.output.pop()

    def print_queue(self):
        for i in range(self.input.top+1):
            temp = self.input.pop()
            self.output.push(temp)

        self.output.print_stack()


q = Queue(5)
q.pop()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
q.print_queue()
q.pop()
q.pop()
q.pop()
q.print_queue()
