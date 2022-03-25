import sys

cnt = int(sys.stdin.readline())
moneyArr = []

for i in range(0, cnt):
    s = int(sys.stdin.readline())
    if s == 0:
        moneyArr.pop()
    else:
        moneyArr.append(s)

print(sum(moneyArr))