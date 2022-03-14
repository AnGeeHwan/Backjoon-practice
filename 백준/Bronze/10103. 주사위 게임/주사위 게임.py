cnt = int(input())

scoreA= 100
scoreB= 100

for i in range(0, cnt):
  a, b = map(int, input().split())

  if a < b:
    scoreA -= b
  elif a > b:
    scoreB -= a


print(scoreA)
print(scoreB)