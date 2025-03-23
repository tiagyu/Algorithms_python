# 문자열 정렬하기 (2)
def solution(my_string):
    my_string = my_string.lower()
    my_string = sorted(my_string)
    answer = "".join(my_string)
    return answer
