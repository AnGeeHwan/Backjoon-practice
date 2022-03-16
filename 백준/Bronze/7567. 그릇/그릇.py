dish = input()
dish = list(dish)
lastDish = ""
height = 0

for i in range(0, len(dish)):
  if dish[i] == lastDish:
    height+=5
  else:
    lastDish = dish[i]
    height+=10

print(height)