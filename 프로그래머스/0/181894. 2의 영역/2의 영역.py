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