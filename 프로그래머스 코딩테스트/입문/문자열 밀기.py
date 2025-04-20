# 문자열 밀기
def solution(A, B):
    a_list = list(A)
    answer = 0

    for _ in range(len(A)):
        if "".join(a_list) == B:
            return answer
        last = a_list.pop()
        a_list.insert(0, last)
        answer += 1
    return -1

# 다른 사람 풀이1
from collections import deque

def solution(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1