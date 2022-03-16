cnt = int(input())
resList = []
res = 0.00
for i in range(0, cnt):
  s = input()
  s = s.split()
  for i in range(0, len(s)):
    if i == 0:
      res = float(s[i])  
    if s[i] == "@":
      res = res * 3
    elif s[i] == "%":
      res = res + 5
    elif s[i] == "#":
      res = res - 7    
  resList.append(res)

for i in range(0, len(resList)):
  print(f'{resList[i]:.2f}')
  
