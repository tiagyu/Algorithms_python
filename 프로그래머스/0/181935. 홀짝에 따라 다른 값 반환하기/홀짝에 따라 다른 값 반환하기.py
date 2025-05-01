def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % 2 == 0:
            if i % 2 == 0:
                answer += i ** 2
        else:
            if i % 2 != 0:
                answer += i
    return answer