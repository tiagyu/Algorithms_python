# 조건 문자열
def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return int(bool(n <= m))
        else:
            return int(bool(n < m))
    else:
        if eq == "=":
            return int(bool(n >= m))
        else:
            return int(bool(n > m))
        
# 다른 사람 풀이1
def solution1(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!','')+str(m)))

# 다른 사람 풀이2
def solution2(ineq, eq, n, m):
    answer = 0
    if n > m and ineq == ">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1
    return answer