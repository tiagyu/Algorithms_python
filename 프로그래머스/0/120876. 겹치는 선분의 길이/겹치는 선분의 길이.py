def solution(lines):
    points = [0] * 201
    for start, end in lines:
        for i in range(start, end):
            points[i + 100] += 1

    answer = sum(1 for x in points if x >= 2)
    return answer
