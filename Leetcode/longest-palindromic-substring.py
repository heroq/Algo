# 접근 및 구현 자체를 실패

def longestPalindrome(s: str) -> str:
    # 가상의 문자 추가
    modified_s = '#'.join('#' + s + '#')
    print(modified_s)

    # 팰린드롬 반경 배열 초기화
    n = len(modified_s)
    print(n)

    # 개수 만큼 배열 생성
    radius = [0] * n
    print(radius)

    # 중심과 우측 경계 초기화
    center, right = 0, 0

    max_radius, max_center = 0, 0

    for i in range(n):
        if i < right:
            mirror = 2 * center - i
            radius[i] = min(right - i, radius[mirror])

        # 팰린드롬 확장
        a, b = i + (1 + radius[i]), i - (1 + radius[i])
        while a < n and b >= 0 and modified_s[a] == modified_s[b]:
            radius[i] += 1
            a += 1
            b -= 1

        # 중심과 우측 경계 갱신
        if i + radius[i] > right:
            center, right = i, i + radius[i]

        # 최장 팰린드롬 갱신
        if radius[i] > max_radius:
            max_radius, max_center = radius[i], i

    # 최장 팰린드롬을 가져옴
    start = (max_center - max_radius) // 2
    end = start + max_radius
    return s[start:end]


print(longestPalindrome("babad"))
