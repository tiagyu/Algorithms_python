# 정수 찾기
def solution(num_list, n):
    for i in num_list:
        if i == n:
            return 1
    return 0


# 다른 사람 풀이1
def solution1(num_list, n):
    return int(n in num_list)


# 다른 사람 풀이2
def solution2(num_list, n):
    answer = 0
    if n in num_list:
        answer = 1
    else:
        answer = 0
    return answer
