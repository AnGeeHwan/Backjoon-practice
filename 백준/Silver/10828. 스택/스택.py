import sys

cnt = int(sys.stdin.readline())
stackArr = []

for i in range(0, cnt):
    s = sys.stdin.readline()
    if(s.find('push') != -1):
        pushNum = s.split()
        stackArr.append(pushNum[1])
    elif(s.find('pop') != -1):
        if len(stackArr) == 0:
            print('-1')
        else:
            print(stackArr.pop())
    elif(s.find('size') != -1):
        print(len(stackArr))
    elif(s.find('empty') != -1):
        if len(stackArr) == 0:
            print('1')
        else:
            print('0')
    elif(s.find('top') != -1):
        if len(stackArr) == 0:
            print('-1')
        else:
            print(stackArr[len(stackArr)-1])

