# 숫자 찾기
def solution(num, k):
    answer = 0
    if str(k) not in str(num):
        answer = -1
    else:
        answer = str(num).index(str(k)) + 1
    return int(answer)

# 다른 사람 풀이1
def solution1(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

# 다른 사람 풀이2
def solution2(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1