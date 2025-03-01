# 구슬을 나누는 경우의 수
import math

def solution(balls, share):
    n = int(balls)
    m = int(share)
    
    # 조합 경우의 수
    n_fact = math.factorial(n)
    n_m_fact = math.factorial(n-m)
    m_fact = math.factorial(m)
    
    return int(n_fact / (n_m_fact * m_fact))

# math 라이브러리의 조합 이용
def solution2(balls, share):
    return math.comb(balls, share)

# 팩토리얼을 직접 만들기
def solution3(balls, share):
    return int(factorial(balls) / (factorial(balls-share) * factorial(share)))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
