def solution(my_string, queries):
    list_my_string = list(my_string)

    for s,e in queries:
        list_my_string[s:e+1] = list_my_string[s:e+1][::-1]

    answer = "".join(list_my_string)
    return answer