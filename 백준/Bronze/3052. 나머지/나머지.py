a = []

for i in range(0, 10):
    inputValue = int(input())
    a.append(inputValue % 42)

result = set(a)
print(len(result))