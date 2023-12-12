# 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 단일 링크드리스트
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 마지막 삽입
    def append(self, data):
        new_node = Node(data)  # 노드 생성

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    # 첫번째 삽입
    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # 삭제
    def remove(self, data):
        linked = self.head
        prev_node = None

        while linked is not None:
            if linked.data == data:

                if self.head == linked:
                    self.head = linked.next

                if self.tail == linked:
                    self.tail = prev_node

                prev_node.next = linked.next
                linked = None

            prev_node = linked

            if linked is not None:
                linked = linked.next


temp = SinglyLinkedList()
temp.append(1)
temp.append(2)
temp.append(3)
temp.prepend(99)
temp.append(4)
temp.prepend(98)
temp.remove(3)

iterator = temp.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
