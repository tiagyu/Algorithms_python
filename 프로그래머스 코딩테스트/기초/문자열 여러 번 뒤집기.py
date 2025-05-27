# 문자열 여러 번 뒤집기
def solution(my_string, queries):
    list_my_string = list(my_string)

    for s,e in queries:
        list_my_string[s:e+1] = list_my_string[s:e+1][::-1]

    answer = "".join(list_my_string)
    return answer

# 다른 사람 풀이1
def solution1(my_string, queries):
    for s,e in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string