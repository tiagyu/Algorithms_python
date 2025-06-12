# 가까운 1 찾기
def solution(arr, idx):
    for i in range(len(arr)):
        if i >= idx and arr[i]==1:
            return i
    return -1

# 다른 사람 풀이1
def solution1(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1
    return answer

# 다른 사람 풀이2
def solution2(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1