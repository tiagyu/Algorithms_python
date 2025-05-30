def solution(my_string):
    answer = []
    list_string = list(my_string)

    while len(list_string) > 0:
        answer.append("".join(list_string))
        list_string.pop(0)
    return sorted(answer)