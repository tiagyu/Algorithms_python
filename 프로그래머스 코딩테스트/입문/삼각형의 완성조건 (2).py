# 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    for i in range(sum(sides)):
        # case 1
        if min(sides) + i > max(sides) and i <= max(sides):
            answer += 1
        # case 2
        elif sum(sides) > i and i > max(sides):
            answer += 1
    return answer

# 다른 사람 풀이
def solution1(sides):
    return sum(sides) - max(sides) + min(sides) - 1