# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for string in my_string:
        if string not in answer:
            answer += string
    return answer

# 다른 사람 풀이 1
def solution2(my_string):
    return "".join(dict.fromkeys(my_string))

# 다른 사람 풀이 2
def solution2(my_string):
    answer = []
    for i in my_string:
        if answer.count(i) == 0:
            answer.append(i)
    return "".join(answer)