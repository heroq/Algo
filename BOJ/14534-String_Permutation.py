import itertools
import sys

count = int(sys.stdin.readline())
str_list = list(sys.stdin.readline().replace("\n", "") for _ in range(count))

for i in range(len(str_list)):
    print("Case # " + str(i + 1) + ":")

    # 순열을 담는다.
    per = itertools.permutations(str_list[i], len(str_list[i]))

    # 출력
    for p in per:
        print(''.join(p))