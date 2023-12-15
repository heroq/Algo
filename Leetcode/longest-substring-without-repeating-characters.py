
testcase = "pwwkew"

used = {}
max_length = start = 0

for i, char in enumerate(testcase):
    # 존재 할 경우
    if char in used and start <= used[char]:
        start = used[char] + 1
    # 존재 하지 않을 경우
    else:
        # 비교해서 큰 값을 가져옴
        max_length = max(max_length, i - start + 1)

    used[char] = i

print(max_length)

