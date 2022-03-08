a = int(input())
sameCnt = 0
resArr = []

for i in range(0, a):
  s = input()
  sumRes = 0
  sameCnt = 0
  for j in s:
    if j == "O":
      sameCnt=sameCnt + 1
      if sameCnt != 0:
        sumRes += sameCnt
      else:
        sumRes +=  1
    else:
      sameCnt = 0
  
  resArr.append(sumRes)

for i in resArr:
  print(i)