def solution(chicken):
    answer = 0
    remainder = 0

    while chicken > 1:
        answer += chicken // 10
        remainder += chicken % 10
        chicken /= 10

    while int(remainder) >= 10:
        answer += remainder // 10
        remainder /= 10
    return answer