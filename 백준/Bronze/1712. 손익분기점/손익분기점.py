import math

a, b, c = map(int, input().split())

if b >= c:
  answer = -1
else:
  answer = a / (c-b) + 1

print(math.floor(answer))

