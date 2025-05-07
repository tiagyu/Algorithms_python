# 정사각형으로 만들기
def solution(arr):
    if len(arr) != len(arr[0]):
        # 행이 열보다 숫자가 큰 경우
        if len(arr) > len(arr[0]):
            while len(arr) > len(arr[0]):
                for i in range(len(arr)):
                    arr[i].append(0)
        # 열이 행보다 숫자가 큰 경우
        if len(arr) < len(arr[0]):
            while len(arr) < len(arr[0]):
                arr.append([0] * len(arr[0]))
        return arr
    return arr

# 다른 사람 풀이1
def solution1(arr):
    n = len(arr)
    m = len(arr[0])
    if n > m:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
    else:
        for i in range(m-n):
            arr.append([0] * m)
    return arr

# 다른 사람 풀이2
def solution2(arr):
    row, col = len(arr), len(arr[0])
    
    if row > col:
        diff = row - col
        for i in range(row):
            arr[i].extend([0] * diff)
    elif row < col:
        diff = col - row
        for _ in range(diff):
            arr.append([0] * col)
    
    return arr