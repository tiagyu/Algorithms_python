# 문자열의 뒤의 n글자
def solution(my_string, n):
    answer = my_string[len(my_string)-n:]
    return answer

# 다른 사람 풀이1
def solution1(my_string, n):
    return my_string[-n:]