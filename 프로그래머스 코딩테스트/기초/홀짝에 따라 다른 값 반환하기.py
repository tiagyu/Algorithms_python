# 홀짝에 따라 다른 값 반환하기
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

# 다른 사람 풀이1
def solution1(n):
    if n % 2:
        return sum(range(1,n+1,2))
    return sum([i * i for i in range(2, n+1, 2)])

# 다른 사람 풀이2
def solution2(n):
    answer = 0
    if n % 2:
        for i in range(1, n+1, 2):
            answer += i
    else:
        for i in range(2, n+1, 2):
            answer += i ** 2
    return answer