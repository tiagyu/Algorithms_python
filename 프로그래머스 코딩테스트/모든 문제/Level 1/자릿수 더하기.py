# 자릿수 더하기
def solution(n):
    answer = sum([int(num) for num in list(str(n))])
    return answer

# 다른 사람 풀이1
def solution1(number):
    return sum([int(i) for i in str(number)])

# 다른 사람 풀이2
def solution2(number):
    return sum(map(int, str(number)))