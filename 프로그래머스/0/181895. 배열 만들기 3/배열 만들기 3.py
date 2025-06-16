def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    answer = []
    for i in range(a1,b1+1):
        answer.append(arr[i])
    for i in range(a2,b2+1):
        answer.append(arr[i])
    return answer