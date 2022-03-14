cnt = int(input())
vote = []

for i in range(0, cnt):
  a = input()
  vote.append(a)

print("Junhee is cute!") if vote.count("1") > vote.count("0") else print("Junhee is not cute!")