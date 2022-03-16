s = input()

checkList= [ "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
wordCnt = 0

# checkList에서 체크 후 변환시 사이 단어가 사라지면서 앞 뒤 문자가 연결되어 인식되는 것을 방지하기위한 " " 구분 삽입
for i in range(0, len(checkList)):
  if s.count(checkList[i]) != 0:
      wordCnt = wordCnt + s.count(checkList[i])
      s = s.replace(checkList[i], " ")

# 단어길이 체크에 " " 구분 삽입된 부분이 포함되어 제거
s = s.replace(" ", "")

if len(s) != 0:
  wordCnt += len(s)

print(wordCnt)