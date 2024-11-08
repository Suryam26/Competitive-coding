class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            if val < self.stack[-1][1]:
                return self.stack.append((val, val))

            return self.stack.append((val, self.stack[-1][1]))

        return self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min())
stack.pop()
print(stack.top())
print(stack.get_min())
