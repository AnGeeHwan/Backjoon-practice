cnt = int(input())
price = []

for i in range(0, cnt):
  s = input().split()
  if s.count(max(s)) == 1:
    price.append(int(max(s))*100)
  elif s.count(max(s)) == 2:
    price.append(1000+int(max(s))*100)
  elif s.count(max(s)) == 3:
    price.append(10000+int(max(s))*1000)

print(max(price))