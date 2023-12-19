# 스택을 사용해서 푸는 문제
# 괄호가 제대로 닫혔는지 확인 하는 문제다.

import sys

N = int(sys.stdin.readline())

bracket_opener = {
    ")": "("
}

for _ in range(N):
    bracket = str(sys.stdin.readline())
    stack = []
    for s in bracket:

        if s == ")":
            if not stack:
                stack.append(s)
                break

            close = stack.pop()
            if bracket_opener[s] != close:
                break
            continue
        elif s == "(":
            stack.append(s)

    if stack:
        print("NO")
    else:
        print("YES")
