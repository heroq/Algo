import heapq
import sys

heap = []
num_count = int(sys.stdin.readline())
for _ in range(num_count):
    num = int(sys.stdin.readline())
    # 힙이 없는데 출력 할 경우
    if not heap and num == 0:
        print(0)
        continue

    # 0 이상 이면 값을 추가
    if num > 0:
        heapq.heappush(heap, num)

    # 힙이 있으면 출력
    if heap and num == 0:
        print(heapq.heappop(heap))