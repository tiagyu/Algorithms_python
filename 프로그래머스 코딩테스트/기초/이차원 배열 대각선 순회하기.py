# 이차원 배열 대각선 순회하기
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer


# 다른 사람 풀이1
def solution1(board, k):
    answer = 0
    n, m = len(board), len(board[0])

    for i in range(n):
        for j in range(m):
            if i + j <= k:
                answer += board[i][j]
            else:
                break
    return answer


# 다른 사람 풀이2
def solution2(board, k):
    return sum(
        board[i][j]
        for i in range(len(board))
        for j in range(len(board[0]))
        if i + j <= k
    )
