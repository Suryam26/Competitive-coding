class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1
        self.overflow = "Overflow: stack is full"
        self.underflow = "Underflow: stack is empty"

    def get_top(self):
        if self.top == -1:
            print(self.underflow)
        return self.stack[self.top]

    def push(self, element):
        if self.top == self.size-1:
            print(self.overflow)
            return
        self.top += 1
        self.stack[self.top] = element
        # print("Element added:", element)

    def pop(self):
        if self.top == -1:
            print(self.underflow)
            return -1
        temp = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return temp

    def print_stack(self):
        for i in range(self.top, -1, -1):
            if self.stack[i]:
                print(self.stack[i], end=" ")
        print()


# s = Stack(5)
# s.pop()
# s.push(5)
# s.push(4)
# s.push(3)
# s.push(2)
# s.push(1)
# s.push(8)
# s.print_stack()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.print_stack()
