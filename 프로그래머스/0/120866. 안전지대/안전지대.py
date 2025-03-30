# 안전지대
def solution(board):
    # 변수 설정
    answer = 0
    new_board = [row [:] for row in board]
    directions = [(-1,-1), (-1,0), (-1,1),
                (0,-1), (0,0), (0,1),
                (1,-1), (1,0), (1,1)]

    for row , i in enumerate(board):
        for column, j in enumerate(i):
            if j == 1 :
                # 좌표 순회회
                for dx, dy in directions:
                    nx, ny = row + dx, column + dy
                    # 범위 확인
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        new_board[nx][ny] += 1
    # 0값 찾기기
    for row in new_board:
        answer += row.count(0)
    return answer

        