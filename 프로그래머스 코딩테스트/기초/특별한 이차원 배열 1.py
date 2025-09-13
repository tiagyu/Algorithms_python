# 특별한 이차원 배열 1
def solution(n):
    answer = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return answer


# 다른 사람 풀이1
def solution1(n):
    answer = [[0] * n for i in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer


# 다른 사람 풀이2
import numpy as np


def solution(n):
    return np.eye(n).tolist()
