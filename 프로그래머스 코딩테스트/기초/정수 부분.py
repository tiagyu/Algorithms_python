# 정수 부분
def solution(flo):
    return int(flo)


# 다른 사람 풀이1
def solution1(flo):
    return flo // 1


# 다른 사람 풀이2
def solution3(flo):
    ans = str(flo).split(".")[0]
    return int(ans)
