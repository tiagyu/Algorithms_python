# 콜라 문제
def solution(a, b, n):
    answer = 0
    while n // a > 0:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer

# 다른 사람 풀이1
solution1 = lambda a, b, n: max(n - b, 0) // (a - b) * b

# 다른 사람 풀이2
def solution2(a, b, n):
    answer = 0
    while n >= a:
        n -= a
        answer += b
        n += b    
    return answer