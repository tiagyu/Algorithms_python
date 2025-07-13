def solution(n):
    n = (n ** 0.5)
    if n.is_integer():
        return int((n+1) ** 2)
    else:
        return -1