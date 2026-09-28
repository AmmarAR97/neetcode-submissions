class MinStack:

    def __init__(self):
        self.stack = []
        self.mininum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mininum_stack:
            self.mininum_stack.append(val)
        else:
            mininum_val = min(self.mininum_stack[-1], val)
            self.mininum_stack.append(mininum_val)

    def pop(self) -> None:
        self.stack.pop()
        self.mininum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mininum_stack[-1]
