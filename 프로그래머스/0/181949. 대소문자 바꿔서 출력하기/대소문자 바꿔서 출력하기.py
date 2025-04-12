str = input()
answer = ""

for i in str:
    if i.isupper():
        i = i.lower()
        answer += i
    else:
        i = i.upper()
        answer += i

print(answer)