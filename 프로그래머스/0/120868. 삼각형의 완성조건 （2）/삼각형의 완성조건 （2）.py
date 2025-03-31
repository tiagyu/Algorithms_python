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