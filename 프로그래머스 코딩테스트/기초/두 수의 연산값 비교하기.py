# 두 수의 연산값 비교하기
def solution(a, b):
    return int(str(a)+str(b)) if int(str(a)+str(b)) >= (2 * a * b) else (2 * a * b)

# 다른 사람 풀이
def solution1(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)