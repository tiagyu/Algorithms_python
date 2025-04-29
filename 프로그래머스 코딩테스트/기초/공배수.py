# 공배수
def solution(number, n, m):
    if number % n == 0:
        if number % m == 0:
            return 1
    return 0

# 다른 사람 풀이1
def solution1(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))

# 다른 사람 풀이2
def solution2(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0