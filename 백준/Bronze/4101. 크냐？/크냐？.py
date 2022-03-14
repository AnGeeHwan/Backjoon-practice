answer = []

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  else:
    answer.append("Yes" if a > b else "No")

for i in answer:
  print(i)