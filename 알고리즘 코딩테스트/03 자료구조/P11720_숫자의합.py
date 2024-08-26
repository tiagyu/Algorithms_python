# 001 숫자의 합 구하기
n = int(input())
numbers = list(input())
answer = 0

for i in numbers:
    answer+=int(i)

print(answer)