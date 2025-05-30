# 접미사 배열
def solution(my_string):
    answer = []
    list_string = list(my_string)

    while len(list_string) > 0:
        answer.append("".join(list_string))
        list_string.pop(0)
    return sorted(answer)

# 다른 사람 풀이1
def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))

# 다른 사람 풀이2
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    answer.sort()
    return answer