# n개 간격의 원소들
def solution(num_list, n):
    answer = answer = [num_list[i] for i in range(0,len(num_list),n)]
    return answer

# 다른 사람 풀이1
def solution1(num_list, n):
    return num_list[::n]