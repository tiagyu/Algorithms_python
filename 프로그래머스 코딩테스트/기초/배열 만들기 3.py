# 배열 만들기 3
def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    answer = []
    for i in range(a1,b1+1):
        answer.append(arr[i])
    for i in range(a2,b2+1):
        answer.append(arr[i])
    return answer

# 다른 사람 풀이1
def solution1(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]

# 다른 사람 풀이2
def solution2(arr, intervals):
    answer = []
    for a,b in intervals: 
        answer+=arr[a:b+1]
    return answer