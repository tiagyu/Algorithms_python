def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        letter = my_string[i]
        answer += letter
    return answer