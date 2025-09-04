# 문자열 정수의 합
def solution(num_str):
    answer = sum([int(i) for i in num_str])
    return answer


# 다른 사람 풀이1
def solution1(num_str):
    return sum(map(int, list(num_str)))


# 다른 사람 풀이2
solution = lambda s: sum(map(int, s))
