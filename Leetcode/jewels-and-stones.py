import collections
jewels, stones = "aA", "aAAbbbb"
stones = collections.Counter(stones)
count = 0
for i in jewels:
    count += stones[i]

print(count)