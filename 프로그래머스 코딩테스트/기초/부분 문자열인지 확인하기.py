# 부분 문자열인지 확인하기
def solution(my_string, target):
    if target in my_string:
        return 1
    return 0


# 다른 사람 풀이1
def solution1(my_string, target):
    return int(target in my_string)


# 다른 사람 풀이2
def solution2(my_string, target):
    answer = 0

    my_string2 = list(my_string)

    for _ in range(len(my_string)):
        if my_string2[: len(target)] == list(target):
            return 1
        my_string2.pop(0)

    return answer
