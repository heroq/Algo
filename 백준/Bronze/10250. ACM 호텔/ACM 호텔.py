import sys

n = int(sys.stdin.readline())

for _ in range(n):
    # H, W, IN
    a, b, c = map(int, sys.stdin.readline().split())

    room = 1
    floor = 1

    while c > 1: # 2
        # 층수를 넘어서면 1층으로
        if floor >= a:
            floor = 1

            # 호수 증가
            room += 1
        # 안넘어서면 더 해 줌
        else:
            floor += 1

        c -= 1

    room = str(room).zfill(2)
    print(f"{floor}{room}")


