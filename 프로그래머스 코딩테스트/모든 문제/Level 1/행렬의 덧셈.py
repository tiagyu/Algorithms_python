# 행렬의 덧셈
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer


arr1, arr2 = [[1, 2], [2, 3]], [[3, 4], [5, 6]]
print(list(zip(arr1, arr2)))


# 다른 사람 풀이1
def solution1(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer


# 다른 사람 풀이2
import numpy as np


def solution2(A, B):
    A_np = np.array(A)
    B_np = np.array(B)
    result = A_np + B_np
    return result.tolist()


# 다른 사람 풀이3
def solution3(A, B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]
