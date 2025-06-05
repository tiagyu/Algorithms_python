def solution(my_string, s, e):
    list_my_string = list(my_string)
    answer = "".join(list_my_string[:s]) + "".join(list_my_string[s:e+1][::-1]) + "".join(list_my_string[e+1:])
    return answer