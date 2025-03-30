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

# 다른 사람 풀이1
def solution1(board):
    n = len(board)
    danger = set()
    for i,row in enumerate(board):
        for j,x in enumerate(board):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1,0,1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i,j in danger)

# 다른 사람 풀이2
def solution2(board):
    answer = 0
    
    for col in range(len(board)):
        for row in range(len(board)):
            if board[row][col] == 1:
                for j in range(max(col-1,0), min(col+2, len(board))):
                    for i in range(max(row-1,0), min(row+2, len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)
    return answer