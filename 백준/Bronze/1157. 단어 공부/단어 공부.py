a = input().upper()

a = list(a)
b = list(set(a))

bCnt = []
answer = ""

for i in b:
    bCnt.append(a.count(i))

if bCnt.count(max(bCnt)) != 1:
    answer = "?"
else:
    answer = b[bCnt.index(max(bCnt))]

print(answer)