# 스택이 2개 쓰이는듯 ?
import collections

# 설거지할걸 5개를 쌓고

# 3번째 위치까지 설거지를 한다고함


# 각 메인 입력 줄에는 명령어 C_i(1 <= C_i <= 2)가 포함되며,
# 여기서 1은 상연이 세척, 2는 병렬이 건조를 나타내고,
# 세척 또는 건조할 설거지 D_i(1 <= D_i <= N)의 개수가 모두 포함됩니다.

cnt = int(input()) + 1
n = collections.deque(range(1, cnt))
wash = collections.deque()
dry = collections.deque()

while True:
    x, y = map(int, input().split())

    for _ in range(y):
        # 세척
        if x == 1:
            wash.append(n.popleft())

        # 건조
        else:
            dry.append(wash.pop())

    if len(dry) == cnt-1:
        break

for i in reversed(dry):
    print(i)