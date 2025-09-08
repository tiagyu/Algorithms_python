# 주사위 게임 1
def solution(a, b):
    odd_a = int(a % 2)
    odd_b = int(b % 2)
    if odd_a and odd_b:
        return a**2 + b**2
    elif odd_a or odd_b:
        return 2 * (a + b)
    else:
        return abs(a - b)


# 다른 사람 풀이1
def solution1(a, b):
    if a % 2 and b % 2:
        return a * a + b * b
    elif a % 2 or b % 2:
        return 2 * (a + b)
    return abs(a - b)


# 다른 사람 풀이2
def solution2(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a * a + b * b
    elif a % 2 == 1 or b % 2 == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)
