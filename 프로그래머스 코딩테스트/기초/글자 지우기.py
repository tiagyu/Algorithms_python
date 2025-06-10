# 글자 지우기
def solution(my_string, indices):
    list_my_string = list(my_string)
    for i in indices:
        list_my_string[i] = ""

    answer = "".join(list_my_string)
    return answer

# 다른 사람풀이1
def solution1(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer

# 다른 사람풀이2
def solution2(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)