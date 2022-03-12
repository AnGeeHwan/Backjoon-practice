a = input()

answer = 0

for i in a:
    if "ABC".find(i) != -1:
        answer = answer + 2
    elif "DEF".find(i) != -1:
        answer = answer + 3
    elif "GHI".find(i) != -1:
        answer = answer + 4
    elif "JKL".find(i) != -1:
        answer = answer + 5
    elif "MNO".find(i) != -1:
        answer = answer + 6
    elif "PQRS".find(i) != -1:
        answer = answer + 7
    elif "TUV".find(i) != -1:
        answer = answer + 8
    elif "WXYZ".find(i) != -1:
        answer = answer + 9    
    answer = answer + 1

print(answer)