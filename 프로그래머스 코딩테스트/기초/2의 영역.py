# 2의 영역
def solution(arr):
    answer = []
    try:
        start = arr.index(2)
    except ValueError:
        return [-1]
    
    for i in range(len(arr)):
        if arr[i] == 2:
            end = i
    for i in range(start,end+1):
        answer.append(arr[i])
    
    return answer

# 다른 사람 풀이 1
def solution1(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

# 다른 사람 풀이 2
def solution2(arr):
    check = []
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0,len(arr)):
            if arr[i] == 2:
                check.append(i)
    return arr[check[0]:check[-1]+1]