# 카운트 다운
def solution(start_num, end_num):
    answer = reversed([i for i in range(end_num, start_num+1)])
    return list(answer)

# 다른 사람 풀이1
def solution1(start, end):
    return list(range(start,end-1,-1))

# 다른 사람 풀이2
def solution2(start, end):
    answer = []
    while start>=end:
        answer.append(start)
        start-=1        
    return answer