# 시간초과
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

strsArr = []

# 문자를 반복
for s in strs:
    tempArr = [s]
    if len(strsArr) == 0:
        strsArr.append(tempArr)
    else:
        # 저장된 문자를 반복
        count = 0
        for x in range(len(strsArr)):
            if ''.join(sorted(strsArr[x][0])) == ''.join(sorted(s)):
                strsArr[x].append(s)
                count = 1

        if count == 0:
            strsArr.append(tempArr)

strsArr = sorted(strsArr)
sortStrsArr = [sorted(row) for row in strsArr]
print(sorted(sortStrsArr, key=len))