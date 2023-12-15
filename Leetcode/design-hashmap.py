import collections


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.table = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        if self.table[key].val is None:
            self.table[key] = Node(key, value)
            return
        self.table[key].val = value

    def get(self, key: int) -> int:
        if self.table[key].val is None:
            return -1
        return self.table[key].val

    def remove(self, key: int) -> None:
        self.table[key] = Node()