import sys

price = int(sys.stdin.readline())

price = 1000 - price

changeArr = [500,100,50,10,5,1]
paperCnt = 0

for i in changeArr:
  changeCnt = price // i
  paperCnt = paperCnt+changeCnt
  price = price - (i * changeCnt)

print(paperCnt)