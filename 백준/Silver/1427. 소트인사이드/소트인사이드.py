import sys

s = list(sys.stdin.readline().replace('\n', ""))
s = list(map(int, s))
s.sort(reverse=True)
print(''.join(map(str, s)))

