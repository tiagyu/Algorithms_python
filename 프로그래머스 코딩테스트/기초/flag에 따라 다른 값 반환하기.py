# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag:
        answer = a+b
    else:
        answer = a-b
    return answer

# 다른 사람 풀이1
def solution1(a, b, flag):
    if flag: return a+b
    return a-b

# 다른 사람 풀이2
def solution2(a, b, flag):
    return a+b if flag else a-b