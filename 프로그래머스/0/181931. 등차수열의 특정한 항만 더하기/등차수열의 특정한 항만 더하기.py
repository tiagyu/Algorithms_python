def solution(a, d, included):
    answer = 0
    true, false = True, False
    for i in range(len(included)):
        if included[i]:
            answer += a
        a += d
    return answer