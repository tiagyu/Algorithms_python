# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for number in numbers:
        answer += number
        if answer > n:
            return answer

# 다른 사람 풀이1
def solution1(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)

# 다른 사람 풀이2
def solution2(numbers, n):
    answer = 0
    i=0
    while answer<=n:
        answer+=numbers[i]
        i+=1
    return answer