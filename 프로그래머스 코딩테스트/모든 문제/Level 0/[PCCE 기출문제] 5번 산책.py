# [PCCE 기출문제] 5번 / 산책
def solution(route):
    east = 0
    north = 0

    for i in route:
        if i == "N":
            north += 1
        elif i == "S":
            north -= 1
        elif i == "E":
            east += 1
        elif i == "W":
            east -= 1
    return [east, north]


# 다른 내 풀이
def solution1(route):
    return [
        (route.count("E") - route.count("W")),
        (route.count("N") - route.count("S")),
    ]
