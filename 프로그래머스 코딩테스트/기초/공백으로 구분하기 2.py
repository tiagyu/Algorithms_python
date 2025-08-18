# 공백으로 구분하기 2
def solution(my_string):
    s = my_string.split(" ")
    answer = [i for i in s if i]
    return answer


# 다른 사람 풀이1
def solution1(my_string):
    return [i for i in my_string.split(" ") if i != ""]


# 다른 사람 풀이2
def solution2(my_string):
    answer = my_string.split()
    return answer
