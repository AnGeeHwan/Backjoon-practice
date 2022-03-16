caseCnt = int(input())

winner = []

for case in range(0, caseCnt):
  scoreY = 0
  scoreK = 0

  for i in range(0, 9):
    a, b = map(int, input().split())
    scoreY += a
    scoreK += b

  if scoreY > scoreK:
    winner.append("Yonsei")
  elif scoreY < scoreK:
    winner.append("Korea")
  else:
    winner.append("Draw")

for j in winner:
  print(j)