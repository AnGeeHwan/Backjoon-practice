a = input().strip()

b = a.split(" ")

if b[0] == '':
    print(0)
else:
    print(len(b))