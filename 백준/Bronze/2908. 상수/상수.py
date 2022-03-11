pairNum1, pairNum2 = list(input().split())

changeNum1 = ""
changeNum2 = ""

for i in range(2, -1, -1):
  changeNum1+=pairNum1[i]
  changeNum2+=pairNum2[i]

print(max(changeNum1, changeNum2))