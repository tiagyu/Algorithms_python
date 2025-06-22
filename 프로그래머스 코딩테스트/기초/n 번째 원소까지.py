# n 번째 원소까지
def solution(num_list, n):
    answer = num_list[:n]
    return answer

# 다른 사람 풀이1
def solution1(num_list, n):
    return [v for i,v in enumerate(num_list) if i<n]