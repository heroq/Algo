# 1. 1234를 0번째를 없애는것
# 2. 2를 맨 뒤에 보낼 것
# 3. 반복
# 4. 마지막에 남은 값

import collections

N = input()
queue = collections.deque(i+1 for i in range(int(N)))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(int(queue[0]))
