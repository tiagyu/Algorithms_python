# 세로 읽기
def solution(my_string, m, c):
    answer= []
    for i in range(0,len(my_string),m):
        answer.append(my_string[i:i+m][c-1])
    return "".join(answer)

# 다른 사람 풀이1
def solution(s, m, c):
    return s[c-1::m]

# 다른 사람 풀이2
def solution(my_string, m, c):
    answer = ''
    for i in range(c-1,len(my_string),m): answer+=my_string[i]
    return answer