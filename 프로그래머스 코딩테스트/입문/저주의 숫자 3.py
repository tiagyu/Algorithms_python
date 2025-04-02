# 저주의 숫자 3
def solution(n):
    answer = 0
    num = 0

    while num < n:
        answer += 1

        # 조건
        if answer % 3 == 0 or "3" in str(answer):
            continue

        num += 1
    return answer

# 다른 사람 풀이1
def solution1(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer