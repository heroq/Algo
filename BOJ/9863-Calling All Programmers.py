# 발신자 수, m은 건너띄는 수, k 발신자
# 일단 발신자가 제거되면 그 위치는 더 이상 계산에 사용되지 않습니다.

while True:
    n, m, k = map(int, input().split())

    if n == 0 and m == 0 and k == 0:
        break

    # 7 다음으로 1부터 다시 정렬이 된다.

    # n = 배열개수
    # m = 삭제되는 위치
    # k = 5번 진행

    arr = [i for i in range(1, n + 1)]

    remove_n = 0
    cur = 0

    while remove_n < k:
        cur = (cur + m - 1) % len(arr)
        remove_n += 1
        last = arr.pop(cur)

    if len(arr) == 0:
        print(last)
        continue

    print(last)
