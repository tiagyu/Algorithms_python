# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[len(overwrite_string)+s:]
    return answer