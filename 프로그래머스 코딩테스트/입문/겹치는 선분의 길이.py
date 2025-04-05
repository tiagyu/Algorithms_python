# 겹치는 선분의 길이
def solution(lines):
    points = [0] * 201
    
    for start, end in lines:
        for i in range(start,end):
            points[i+100] += 1
    
    answer = sum(i for x in points if x >= 2)
    return answer

# 다른 사람 풀이  1
def solution1(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 다른 사람 풀이 2
def solution2(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))