import sys

cnt = int(sys.stdin.readline())
change = [[]for row in range(cnt)]

for i in range(0, cnt):
    s = int(sys.stdin.readline())    
    change[i].append(s // 25)
    s = s - (25 * (s//25))
    change[i].append(s // 10)
    s = s - (10 * (s//10))
    change[i].append(s // 5)
    s = s - (5 * (s//5))
    change[i].append(s // 1)
    
for i in range(0, len(change)):
    print(" ".join(str(j) for j in change[i]))