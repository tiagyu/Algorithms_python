# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        letter = my_string[i]
        answer += letter
    return answer

# 다른 사람 풀이1
def solution1(my_string, index_list):
    return "".join([my_string[idx] for idx in index_list])

# 다른 사람 풀이2
def solution2(my_string, index_list):
    return "".join(map(lambda x : my_string[x], index_list))