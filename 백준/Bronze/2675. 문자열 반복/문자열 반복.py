loopCnt = int(input())
answer = ""

for i in range(0, loopCnt):
  if i != 0:
    answer += "\n"
  repeatCnt, repeatStr = input().split()
  repeatStr = list(repeatStr)
  for j in repeatStr:
    answer += j * int(repeatCnt)

print(answer)