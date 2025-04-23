# 문자열 곱하기
def solution(my_string, k):
    answer = my_string * k 
    return answer

# 다른 사람 풀이
solution1 = lambda my_string, k : "".join([my_string, k])