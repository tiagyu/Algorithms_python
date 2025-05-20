# 콜라츠 수열 만들기
def solution(n):
    answer = []
    while n != 1:
        answer.append(int(n))
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
    answer.append(1)
    return answer

# 다른 사람 풀이1
def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer