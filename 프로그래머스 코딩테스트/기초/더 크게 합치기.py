# 더 크게 합치기
def solution(a, b):
    return int(str(a)+str(b)) if int(str(a)+str(b)) > int(str(b)+str(a)) else int(str(b)+str(a))

# 다른 사람 풀이 1
def solution1(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# 다른 사람 풀이 2
def solution2(a, b):
    a , b = str(a), str(b)
    return int(max(a+b, b+a))