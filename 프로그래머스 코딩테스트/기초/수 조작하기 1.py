# 수 조작하기 1
def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        elif i == "a":
            n -= 10
    return n

# 다른 사람 풀이 1
def solution1(n, control):
    key = dict(zip(['w','s','d','a'],[1,-1,10,-10]))
    return n + sum([key[c] for c in control])

# 다른 사람 풀이 2
def solution2(n, control):
    answer = n
    c = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer