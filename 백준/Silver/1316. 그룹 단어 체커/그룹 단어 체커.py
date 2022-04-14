import sys

cnt = int(sys.stdin.readline())

answerCnt = 0

def wordCheck(n):
  charList = []
  lastChar = ""
  for i in n:
    if lastChar != i:
      if charList.count(i) == 1:
        return False
      lastChar = i
      charList.append(lastChar)  

  return True
    
for i in range(0, cnt):
  word = sys.stdin.readline()

  if wordCheck(word) == True:
    answerCnt += 1
  
print(answerCnt)