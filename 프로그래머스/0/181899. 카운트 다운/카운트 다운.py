def solution(start_num, end_num):
    answer = reversed([i for i in range(end_num, start_num+1)])
    return list(answer)