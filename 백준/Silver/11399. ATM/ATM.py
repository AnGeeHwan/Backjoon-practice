import sys

cnt = int(sys.stdin.readline())
spendTime = sys.stdin.readline()
answer = 0
spend = 0
spendTime = list(map(int, spendTime.split()))
spendTime.sort()

for i in spendTime:
    spend = spend + i
    answer += spend

print(answer)