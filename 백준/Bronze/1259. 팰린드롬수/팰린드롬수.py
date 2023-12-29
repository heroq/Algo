import collections
import sys

readline = sys.stdin.readline

while True:
    m = str(readline().strip())
    if m == "0":
        break

    stack = collections.deque()

    for i in m:
        stack.append(i)

    result = True
    while len(stack) > 1:
        x = stack.pop()
        y = stack.popleft()
        # 1221

        if x != y:
            print("no")
            result = False
            break

    if result:
        print("yes")