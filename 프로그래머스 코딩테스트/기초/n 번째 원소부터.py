# n 번째 원소부터
def solution(num_list, n):
    answer = [num_list[i] for i in range(n-1,len(num_list))]
    return answer

# 다른 사람 풀이1
def solution1(num_list, n):
    return num_list[n-1:]

# 다른 사람 풀이2
def solution2(num_list, n):
    answer = []
    for i in range(n-1,len(num_list)):
        answer.append(num_list[i])
    return answer