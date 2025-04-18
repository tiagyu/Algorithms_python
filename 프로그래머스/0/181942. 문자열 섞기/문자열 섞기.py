def solution(str1, str2):
    answer = ''
    str1_list = list(str1)
    str2_list = list(str2)

    for i in range(len(str1)):
        answer += str1_list[i]
        answer += str2_list[i]
    return answer