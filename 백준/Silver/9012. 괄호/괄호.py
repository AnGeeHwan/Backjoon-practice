import sys

cnt = int(sys.stdin.readline())
answer = []

for i in range(0, cnt):
    s = sys.stdin.readline()

    while s.find("()") != -1:
        s = s.replace("()","")

    s = s.strip()
    
    if len(s) != 0:
        answer.append("NO")
    else:
        answer.append("YES")

for i in answer:
    print(i)
