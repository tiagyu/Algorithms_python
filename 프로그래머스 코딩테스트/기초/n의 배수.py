# n의 배수
def solution(num, n):
    if num % n == 0:
        return 1
    return 0

# 다른 사람 풀이1
def solution1(num, n):
    return int(not(num % n))

# 다른 사람 풀이2
def solution2(num, n):
    return int(num % n == 0)