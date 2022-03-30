import sys

cnt = int(sys.stdin.readline())
answer = []
for i in range(0, cnt):
  answer.append(int(sys.stdin.readline()))

answer.sort()

for i in answer:
  print(i)