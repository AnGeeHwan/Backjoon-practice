case = int(input())
resList = []

for i in range(0, case):
  a, b, c = map(int, input().split())

  if a +c > b:
    resList.append("do not advertise")
  elif a + c == b:
    resList.append("does not matter")
  elif a+c < b:
    resList.append("advertise")

for i in resList:
  print(i)