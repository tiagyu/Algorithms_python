def solution(my_string, indices):
    list_my_string = list(my_string)
    for i in indices:
        list_my_string[i] = ""

    answer = "".join(list_my_string)
    return answer