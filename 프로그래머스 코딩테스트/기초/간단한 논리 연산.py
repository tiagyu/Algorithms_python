# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer

# 다른 사람 풀이1
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)