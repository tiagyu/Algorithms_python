# 수열과 구간 쿼리 1
def solution(arr, queries):
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] = arr[i] + 1
    return arr

# 다른 사람 풀이1
def solution1(arr, queries):
    for (s, e) in queries:
        arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr

# 다른 사람 풀이2
import numpy as np

def solution2(arr, queries):
    answer = []

    arr = np.array(arr)
    for query in queries:
        arr[query[0]:query[1] + 1] += 1

    answer = arr.tolist()
    return answer