def solution(my_string, m, c):
    answer= []
    for i in range(0,len(my_string),m):
        answer.append(my_string[i:i+m][c-1])
    return "".join(answer)