# 특별한 이차원 배열 2
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


# 다른 사람 풀이1
def solution1(arr):
    return int(arr == list(map(list, zip(*arr))))


# 다른 사람 풀이2
def solution2(arr):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # 대각선 위에만 검사
            if arr[i][j] != arr[j][i]:
                return 0

    return 1
