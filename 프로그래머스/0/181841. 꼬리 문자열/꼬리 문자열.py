def solution(str_list, ex):
    answer_list = []

    for i in str_list:
        if not ex in i:
            answer_list.append(i)

    answer = "".join(answer_list)
    return answer