dotPosX = []
dotPosY = []

for i in range(0, 3):
  x, y = map(int, input().split())

  if len(dotPosX) == 0 and len(dotPosY) == 0:
    dotPosX.append(x)
    dotPosY.append(y)
  else:
    if dotPosX.count(x) == 0:      
      dotPosX.append(x)
    else:
      dotPosX.remove(x)
    
    if dotPosY.count(y) == 0:
      dotPosY.append(y)
    else:
      dotPosY.remove(y)
    

print(dotPosX[0], dotPosY[0])