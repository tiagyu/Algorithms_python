# 주사위 게임 2
def solution(a, b, c):
    if a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif (a != b) and (a!= c) and (b!=c):
        answer = a + b + c
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    return answer

# 다른 사람 풀이1
def solution1(a, b, c):
    check = len(set([a,b,c]))
    if check == 1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check == 2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return a+b+c

# 다른 사람 풀이2
def solution2(a, b, c):
    list = [a,b,c]
    answer = 1
    for i in range(4-len(set(list))):
        answer *= a**(i+1)+b**(i+1)+c**(i+1)
    return answer