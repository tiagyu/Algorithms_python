# 약수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer

# 다른 사람 풀이1
def solution1(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# 다른 사람 풀이2
def solution2(num):
    return sum([i for i in range(1, num+1) if num % i == 0])