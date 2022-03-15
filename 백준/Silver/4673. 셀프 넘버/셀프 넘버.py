Num = []

for i in range(1, 10001):
  curNum = i
  for j in list(str(i)):
    curNum+=int(j)

  Num.append(str(curNum))

for i in range(1, 10000):
  if str(i) not in Num:
    print((i))