cnt = int(input())

onLine =0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(1, cnt+1):
  a, b = map(int, input().split())

  if a == 0 or b == 0:
    onLine+=1
  elif a > 0 and b > 0:
    q1+=1
  elif a < 0 and b > 0:
    q2+=1
  elif a < 0 and b < 0:
    q3+=1
  else:
    q4+=1

print("Q1: " + str(q1))
print("Q2: " + str(q2))
print("Q3: " + str(q3))
print("Q4: " + str(q4))
print("AXIS: " + str(onLine))