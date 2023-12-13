# 알파벳 개수의 배열을 생성
import collections
import string

# 알파벳의 위치를 알아야하는데 ?
# a,b,c,d,e.. 0,1,2,3,4


# 입력을 받으면
# 1. 알파벳의 위치를 알아야한다.
# 2. 개수를 넣어야한다.


alpha_list = [0] * len(string.ascii_lowercase)

alpha = {}
index = 0
for i in string.ascii_lowercase:
    alpha[i] = index
    index += 1

# N = input()
N = "baekjoon"

for char in N:
    alpha_list[alpha[char]] += 1

print(" ".join(map(str, alpha_list)))