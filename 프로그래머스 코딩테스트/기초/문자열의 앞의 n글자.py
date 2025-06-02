# 문자열의 앞의 n글자
def solution(my_string, n):
    answer = my_string[:n]
    return answer

# 다른 사람 풀이1
def solution1(my_string, n):
    answer = ''
    for i in range(n) :
        answer += my_string[i]
    return answer