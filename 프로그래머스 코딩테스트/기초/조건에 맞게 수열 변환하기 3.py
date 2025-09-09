# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    for i in range(len(arr)):
        if k % 2:
            arr[i] *= k
        else:
            arr[i] += k
    return arr


# 다른 사람 풀이1
def solution1(arr, k):
    return [i * k if k % 2 != 0 else i + k for i in arr]


# 다른 사람 풀이2
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))
