answer = []

while True:  
  s = list(map(int, input().split()))
  s.sort()
  a, b, c = s[0], s[1], s[2]
  
  if a == 0 and b == 0 and c == 0:
    break
  
  if a**2 + b**2 == c**2:
    answer.append("right")
  else:
    answer.append("wrong")

for i in answer:
  print(i)