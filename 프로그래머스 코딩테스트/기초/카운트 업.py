# 카운트 업
def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer

# 다른 사람 풀이1
def solution1(start, end):
    return list(range(start, end + 1))

# 다른 사람 풀이2
def solution2(start, end):
    return [i for i in range(start,end+1)]