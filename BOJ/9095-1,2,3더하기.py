# 정수 4를 1,2,3의 합으로 나타내는 방법의 개수를 출력
# 출처 https://velog.io/@saint6839/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-9095-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0

global count

T = int(input())

def dfs(target, value):
    if target < value:
        return

    if target == value:
        global count
        count += 1
        return
    else:
        dfs(target, value + 1)
        dfs(target, value + 2)
        dfs(target, value + 3)

        # 0
            # 1
                # 2
                    # 3
                        # 4
                        # 5
                        # 6
                    # 4
                    # 5
                # 3
                    # 4
                    # 5
                    # 6
                # 4

            # 2
                # 3
                    # 4
                    # 5
                    # 6
                # 4
                # 5
            # 3
                # 4
                # 5
                # 6

for _ in range(T):
    n = int(input())
    count = 0
    dfs(n, 0)
    print(count)