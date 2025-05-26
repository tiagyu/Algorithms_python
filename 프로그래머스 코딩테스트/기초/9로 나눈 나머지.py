# 9로 나눈 나머지
def solution(number):
    answer = int(number) % 9
    return answer

# 다른 사람 풀이1
def solution1(number):
    return sum(list(map(int, number))) % 9

# 다른 사람 풀이2
def solution2(number):
    n = 0
    for x in number:
        n += int(x)
    return n % 9