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
