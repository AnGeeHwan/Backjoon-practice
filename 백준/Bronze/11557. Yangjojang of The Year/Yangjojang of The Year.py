import sys

case = int(sys.stdin.readline())
answerArr = []

for i in range(0, case):
    univCnt = int(sys.stdin.readline())
    univ = ""
    beer = 0
    for j in range(0, univCnt):
        x, y = map(str, sys.stdin.readline().split())
        if int(y) > beer:
            beer = int(y)
            univ = x
    answerArr.append(univ)

for answer in answerArr:
    print(answer)