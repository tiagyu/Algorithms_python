# 유한소수 판별하기
from fractions import Fraction

def solution(a, b):
    divide_ab = Fraction(a,b)
    d = divide_ab.denominator
    
    while d % 2 == 0:
        d /= 2
    while d % 5 == 0:
        d /= 5
        
    if d == 1:
        return 1
    else:
        return 2

# 다른 사람 풀이1
from math import gcd

def solution1(a,b):
    b //= gcd(a,b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b==1 else 2

# 다른 사람 풀이2
def solution2(a,b):
    answer = 0
    for i in range(2, min([a,b]) + 1):
        while a % i == 0 and b % i == 0:
            a = a//i
            b = b//i
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    if b == 1:
        answer = 1
    else:
        answer = 2
    return 2