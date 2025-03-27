# 캐릭터의 좌표
def solution(keyinput, board):
    x, y = 0,0
    possible_x, possible_y = board[0]//2, board[1]//2

    for move in keyinput:
        if move == "right":
            if x < possible_x:
                x += 1
        elif move == "left":
            if x > -possible_x:
                x -= 1
        elif move == "up":
            if y < possible_y:
                y += 1
        elif move == "down":
            if y > -possible_y:
                y -= 1
    answer = [x,y]            
    return answer

# 다른 사람 풀이1
def solution1(keyinput, board):
    x_lim, y_lim = board[0]//2, board[1]//2
    move = {"left" : (-1,0), "right" : (1,0), "up" : (0,1), "down" : (0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx, dy = move[k]
        if abs(x+dx) > x_lim or abs(y+dy) > y_lim:
            continue
        else:
            x, y = x+dx, y+dy
    return [x,y]