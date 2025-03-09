# 팩토리얼
def solution(n):
    factorial_number = 1
    answer = 0
    for i in range(1, 12):
        factorial_number *= i
        if n < factorial_number:
            answer = i-1
            break
    return answer