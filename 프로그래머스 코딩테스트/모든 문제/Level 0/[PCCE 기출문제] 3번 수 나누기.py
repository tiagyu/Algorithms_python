# [PCCE 기출문제] 3번 / 수 나누기
number = int(input())

answer = 0

for i in range(len(str(number)) // 2):
    answer += number % 100
    number //= 100

print(answer)

# 다른 사람 풀이1
number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(answer)
