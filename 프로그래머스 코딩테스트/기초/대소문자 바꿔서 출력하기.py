# 대소문자 바꿔서 출력하기
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

# 다른 사람 풀이
print(input().swapcase())