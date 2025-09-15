# 콜라츠 추측
def solution(num):
    i = 0
    if num != 1:
        while num != 1 and i <= 500:
            i += 1
            if num % 2 == 0:
                num /= 2
            else:
                num = (num * 3) + 1
        if i > 500:
            return -1
        else:
            return i
    else:
        return 0


# 다른 사람 풀이1
def solution1(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1


# 다른 사람 풀이2
def solution2(num):
    answer = 0
    while answer < 500:
        answer += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        if num == 1:
            break
    if answer == 500:
        answer = -1

    return answer
