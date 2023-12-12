# 싱글 링크드리스트 구현
# 삽입
# 삭제
# 조회

# 노드가 필요하다
# 싱글은 포인터가 한개여서 단일로 하나로만 쭉 간다.
# ㅁ - ㅁ - ㅁ - ㅁ 이면은, 0은 1을 바라보고 1은 2를 바라본다..

class SinglyLinkedList(object):
    def __init__(self):
        self.head = 0
