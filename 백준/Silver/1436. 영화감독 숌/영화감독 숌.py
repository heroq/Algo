import sys

readline = sys.stdin.readline

n = int(readline())
ans = 666
cnt = 0

while True:
    if '666' in str(ans):
        cnt += 1

    if cnt == n:
        break

    ans += 1

print(ans)