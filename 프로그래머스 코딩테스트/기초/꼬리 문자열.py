# 꼬리 문자열
def solution(str_list, ex):
    answer_list = []

    for i in str_list:
        if not ex in i:
            answer_list.append(i)

    answer = "".join(answer_list)
    return answer


# 다른 사람 풀이1
def solution1(str_list, ex):
    return "".join(filter(lambda x: ex not in x, str_list))


# 다른 사람 풀이2
def solution2(str_list, ex):
    filtered_list = [s for s in str_list if ex not in s]
    return "".join(filtered_list)


# 다른 사람 풀이3
def solution3(str_list, ex):
    answer = ""
    for x in str_list:
        if ex in x:
            continue
        answer += x
    return answer
