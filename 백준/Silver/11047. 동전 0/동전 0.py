import sys

cnt, money = map(int, sys.stdin.readline().split())
moneyList = []
coinCnt = 0

for i in range(0, cnt):
    s = int(sys.stdin.readline())
    moneyList.append(s)

for j in range(len(moneyList)-1, -1, -1):
    coinCnt += money // moneyList[j]
    money = money % moneyList[j]

print(coinCnt)