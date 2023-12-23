import itertools
import sys

count = int(sys.stdin.readline())
str_list = list(sys.stdin.readline().replace("\n", "") for _ in range(count))
for i in range(len(str_list)):
    print("Case # " + str(i + 1) + ":")
    per = itertools.permutations(str_list[i], len(str_list[i]))
    for p in per:
        print(''.join(p))