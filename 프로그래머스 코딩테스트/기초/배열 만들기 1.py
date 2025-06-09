# 배열 만들기 1
def solution(n, k):
    answer = [i for i in range(k,n+1,k)]
    return answer

# 다른 사람 풀이1
def solution1(n, k):
    answer = []
    index = 1
    while k * index <= n:
        answer.append(k*index)
        index += 1
    return answer

# 다른 사람 풀이2
def solution2(n, k):
    answer = []
    for i in range(1, n+1):
        if i%k==0:
            answer.append(i)
    return answer