from collections import Counter
import sys

cnt = int(sys.stdin.readline())
inputArr = []


for i in range(0, cnt):
    inputArr.append(int(sys.stdin.readline()))

inputArr.sort()

countArr = Counter(inputArr).most_common()

print(round(sum(inputArr) / cnt))
print(inputArr[cnt//2])

if len(countArr) > 1:
    if countArr[0][1] == countArr[1][1]:
        print(countArr[1][0])
    else:
        print(countArr[0][0])
else:
    print(countArr[0][0])

print(inputArr[-1]-inputArr[0])
