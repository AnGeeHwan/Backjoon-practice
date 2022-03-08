from operator import indexOf
resArr = []

for i in range(0, 9):
  num = int(input())
  resArr.append(num)

print(max(resArr))
print(indexOf(resArr, max(resArr))+1)