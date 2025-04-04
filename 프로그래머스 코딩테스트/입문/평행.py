# 평행
# 기울기 구하는 함수
def calculate_slope(index_1, index_2, dots):
    change_x = abs(dots[index_1][0] - dots[index_2][0])
    change_y = abs(dots[index_1][1] - dots[index_2][1])
    slope = change_y / change_x
    return slope

def solution(dots):
    combinations = [
    [0,1,2,3],
    [0,2,1,3],
    [0,3,1,2]
    ]
    for i in combinations:
        slope_1 = calculate_slope(i[0],i[1],dots)
        slope_2 = calculate_slope(i[2],i[3],dots)
        if slope_1 == slope_2:
            return 1
    return 0

# 다른 사람 풀이1
def solution1(dots):
    [[x1,y1], [x2,y2], [x3,y3], [x4,y4]] = dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0

# 다른 사람 풀이2
from itertools import combinations

def solution2(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))
        
    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2 == x2 *y1:
            return 1
    return 0