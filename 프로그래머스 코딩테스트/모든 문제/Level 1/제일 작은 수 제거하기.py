# 제일 작은 수 제거하기
def solution(arr):
    if len(arr) > 1:
        arr.remove(sorted(arr)[0])
        return arr
    else:
        return [-1]


# 다른 사람 풀이1
def solution1(arr):
    return [i if i > min(arr) else -1 for i in arr]


# 다른 사람 풀이2
def solution2(arr):
    arr.pop(arr.index(min(arr)))
    return arr
