def solution(intStrs, k, s, l):
    answer = []
    for arr in intStrs:
        if k < int(arr[s:s+l]):
            answer.append(int(arr[s:s+l]))
    return answer