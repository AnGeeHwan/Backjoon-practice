a = int(input())
sameCnt = 0
resArr = []

for i in range(0, a):
  s = input()
  sumRes = 0 
  sameCnt = 0
  for j in s:
    if j == "O":      
      if sameCnt != 0:
        sameCnt=sameCnt + 1
        sumRes += sameCnt        
      else:
        sameCnt = 1
        sumRes +=  sameCnt       
    else:
      sameCnt = 0
      
  resArr.append(sumRes)

for i in resArr:
  print(i)
