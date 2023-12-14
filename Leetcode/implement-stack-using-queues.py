import collections


class MyStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
            # 2 1 3
            # 1 3 2
            # 3 2 1

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
