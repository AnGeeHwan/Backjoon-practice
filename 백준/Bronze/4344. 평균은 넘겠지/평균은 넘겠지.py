a = int(input())
resArr = []

for i in range(0, a):
  averScore = 0
  resCnt = 0
  s = list(map(int, input().split()))
  # 사람 수 추출 후 제거
  people = s[0]
  s.remove(s[0])

  averScore = sum(s) / people

  for i in s:
    if i > averScore:
      resCnt+=1

  resRound = round(resCnt / people * 100, 3)
  resArr.append(str('%.3f' % resRound) + "%")

for i in resArr:
  print(i)
