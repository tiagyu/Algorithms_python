# 숫자 찾기
def solution(num, k):
    answer = 0
    if str(k) not in str(num):
        answer = -1
    else:
        answer = str(num).index(str(k)) + 1
    return int(answer)