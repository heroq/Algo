import collections

nums, k = [3,0,1,0], 1
stack = []
for a, b in collections.Counter(nums).most_common():
    if k == 0:
        break
    stack.append(a)
    k -= 1
print(stack)
