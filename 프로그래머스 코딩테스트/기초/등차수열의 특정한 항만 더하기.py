# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a
        a += d
    return answer

# 다른 사람 풀이1
def solution1(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a+d*i) * int(included[i])
    return answer

# 다른 사람 풀이2
def solution2(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)