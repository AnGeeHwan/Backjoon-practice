s = int(input())
cnt = 0

for i in range(1, s+1):
  iArr = list(str(i))

  if len(iArr) <= 2:
    cnt+=1
  elif len(iArr) == 3:
    if int(iArr[0]) - int(iArr[1]) == int(iArr[1]) - int(iArr[2]):
      cnt+=1
  elif len(iArr) == 4:
    if int(iArr[0]) - int(iArr[1]) == int(iArr[1]) - int(iArr[2]) and int(iArr[1]) - int(iArr[2]) == int(iArr[2]) - int(iArr[3]):
      cnt+=1

print(cnt)
