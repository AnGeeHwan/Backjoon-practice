x, y, w, h = map(int, input().split())

minLen = []

minLen.append(w-x)
minLen.append(x-0)
minLen.append(h-y)
minLen.append(y-0)

print(min(minLen))