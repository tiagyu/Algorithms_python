# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2:
            if not i % 2:
                arr[i] += n
        else:
            if i % 2:
                arr[i] += n
    return arr


# 다른 사람 풀이1
def solution1(arr, n):
    N = len(arr)
    if N % 2:
        for i in range(0, N, 2):
            arr[i] += n
    else:
        for i in range(1, N, 2):
            arr[i] += n
    return arr


# 다른 사람 풀이2
def solution2(arr, n):
    if len(arr) % 2:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n

    return arr
