import collections


class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class HashMap:
    def __init__(self):
        self.table = collections.defaultdict(ListNode)
        self.size = 1000

    def put(self, key: int, val: int) -> None:
        # 사이즈가 안넘게 연산 (해싱)
        index = key % self.size

        # 해당 키에 값이 없으면 추가
        if self.table[index].val is None:
            self.table[index] = ListNode(key, val)
            return

        # 값이 존재 하다면
        p = self.table[index]
        while p:
            # 개별 체이닝은 계속 연결 해주는 줄 알았는데
            # 값을 변경해주고 return을 해준다..?
            if p.key == key:
                p.val = val
                return

            if p.next is None:
                break

            p = p.next

        # 노드의 다음으로 계속 이어져가야하는게 아닌가??
        p.next = ListNode(key, val)

    def get(self, key: int):
        index = key % self.size
        p = self.table[index]
        if p.val is None:
            return -1

        # 존재한다면, 값 리턴
        while p:
            if p.key == key:
                return p.val
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].val is None:
            return -1

        # 찾는게 첫번째 위치에 있을 경우
        # p.next가 없으면 빈노드로 만들어준다, 아닐경우 p.next 다음 노드로 간다.

        # 이러면 삭제는 안하고 다음 노드로 self.table[index] 넣어주고 끝인가?
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


test = HashMap()
test.put(1, 1)
test.put(1, 2)
test.remove(1)
test.put(1, 3)
test.put(1, 4)