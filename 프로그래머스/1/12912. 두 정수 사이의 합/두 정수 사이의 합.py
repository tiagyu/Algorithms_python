def solution(a, b):
    if b < a:
        a, b = b, a
    answer = sum([i for i in range(a,b+1)])
    return answer