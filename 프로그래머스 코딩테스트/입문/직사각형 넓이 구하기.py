# 직사각형 넓이 구하기
def solution(dots):
    x_dot = []
    y_dot = []

    for dot in dots:
        # x 좌표
        if dot[0] not in x_dot:
            x_dot.append(dot[0])
        # y 좌표
        if dot[1] not in y_dot:
            y_dot.append(dot[1])
        else:
            pass
    # 넓이 구하기기
    answer = abs(x_dot[0]-x_dot[1]) * abs(y_dot[0]-y_dot[1])
    
    return answer

# 다른 사람 풀이1
def solution1(dots):
    return (max(dots)[0] - min(dots)[1]) * (max(dots)[1] - min(dots)[1])

# 다른 사람 풀이2
def solution2(dots):
    x, y = [], []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    return (max(x) - min(x)) * (max(y) - min(y))