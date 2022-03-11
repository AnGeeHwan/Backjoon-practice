s = input()
answer = ""

for i in range(ord('a'), ord('z')+1):
  if s.find(chr(i)) != -1:
    answer = answer + str(s.index(chr(i))) + " "
  else:
    answer = answer + "-1 "
  
print(answer.rstrip())
