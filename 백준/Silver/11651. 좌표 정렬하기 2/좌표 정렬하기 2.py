from ntpath import join
import sys

case = int(sys.stdin.readline())
answerArr = []

for i in range(case):
    answerArr.append(list(map(int, sys.stdin.readline().split())))

answerArr.sort(key=lambda x: (x[1], x[0]))
        
for i in answerArr:
    print(str(i[0])+ " " + str(i[1]))