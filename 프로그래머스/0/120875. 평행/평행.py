# 평행
# 기울기 구하는 함수수
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