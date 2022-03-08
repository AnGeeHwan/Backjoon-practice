a = int(input())
res = list(map(int, input().split()))
# max값 도출
topRes = max(res)

# 함수화
def sumNum(arrNum):
  return int(arrNum) / int(topRes) * 100

sumArr = list(map(sumNum, res))

sumRes = sum(sumArr) / a

print(sumRes)