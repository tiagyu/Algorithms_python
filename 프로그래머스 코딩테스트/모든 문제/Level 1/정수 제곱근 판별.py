# 정수 제곱근 판별
def solution(n):
    n = (n ** 0.5)
    if n.is_integer():
        return int((n+1) ** 2)
    else:
        return -1
    
# 다른 사람 풀이1
def solution1(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1