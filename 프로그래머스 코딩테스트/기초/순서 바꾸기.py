# 순서 바꾸기
def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    return answer

# 다른 사람 풀이1
def solution1(num_list, n):
    answer = []
    answer.extend(num_list[n:] + num_list[:n])
    return answer

# 다른 사람 풀이2
from collections import deque

def solution3(num_list, n):
    num_list = deque(num_list)
    num_list.rotate(-n)
    return list(num_list)