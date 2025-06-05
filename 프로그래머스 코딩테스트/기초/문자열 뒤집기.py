# 문자열 뒤집기
def solution(my_string, s, e):
    list_my_string = list(my_string)
    answer = "".join(list_my_string[:s]) + "".join(list_my_string[s:e+1][::-1]) + "".join(list_my_string[e+1:])
    return answer

# 다른 사람 풀이1
def solution1(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]

# 다른 사람 풀이2
def solution2(my_string, s, e):
    substr = reversed(list(my_string[s:e+1]))
    return my_string[:s] + ''.join(substr) + my_string[e+1:]