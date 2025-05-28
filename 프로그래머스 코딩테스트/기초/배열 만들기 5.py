# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for arr in intStrs:
        if k < int(arr[s:s+l]):
            answer.append(int(arr[s:s+l]))
    return answer

# 다른 사람 풀이1
def solution1(intStrs, k, s, l):
    return [int(intstr[s:s+l]) for intstr in intStrs if int(intStrs[s:s:+l]) > k ]

# 다른 사람 풀이2
def solution2(intStrs, k, s, l):
    return list(filter(lambda x: x > k, map(lambda x: int(x[s:s+l]), intStrs)))