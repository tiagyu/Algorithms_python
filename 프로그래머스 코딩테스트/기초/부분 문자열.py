# 부분 문자열
def solution(str1, str2):
    return int(str1 in str2)


# 다른 사람 풀이1
def solution1(str1, str2):
    return 1 if str1 in str2 else 0
