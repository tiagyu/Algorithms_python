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

# 다른 사람 풀이 1
from math import factorial

def solution2(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

# 다른 사람 풀이 2
def solution3(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial *= answer
    answer -= 1
    return answer