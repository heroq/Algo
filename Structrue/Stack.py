# 노드로 이어준다.
# 연결할 Stack Class 필요
# top인지 구분을 해야함

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top.data
        self.top = self.top.next
        return node

    def peek(self):
        if not self.top:
            return None

        return self.top.data


stack = Stack()

for i in range(3):
    stack.push(i)
    print(stack.peek())

stack.pop()
stack.pop()