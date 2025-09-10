def solution(n):
    # 1. 2차원 배열을 0으로 만들기
    answer = [[0 for _ in range(n)] for _ in range(n)]

    # 2. 방향에 따른 좌표 미리 구하기
    # 오른쪽 : y+1, 아래 : x+1, 왼쪽 : y-1, 위쪽 : x-1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 3. 현재 위치와 방향을 초기화
    x, y = 0, 0
    direction = 0  # 0 : 오른쪽 , 1 : 아래, 2 : 왼쪽, 3 : 위쪽

    # 4. 배열에 채워 넣기
    for i in range(1, n**2 + 1):
        # 현재 위치에 숫자 넣기
        answer[x][y] = i

        # 다음에 이동할 위치를 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction = (direction + 1) % 4

        x += dx[direction]
        y += dy[direction]
    return answer