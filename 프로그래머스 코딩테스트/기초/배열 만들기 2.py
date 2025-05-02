# 배열 만들기 2
def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if all(d in ['0','5'] for d in list(str(i))):
            answer.append(i)
    return answer if len(answer) > 0 else [-1]

# 다른 사람 풀이1
def solution1(l, r):
    answer = []
    for num in range(l, r+1):
        if not set(str(num)) - set(['0','5']):
            answer.append(num)
    return answer if answer else [-1]

# 다른 사람 풀이2
def solution2(l, r):
    answer = []
    i = 1
    n = 5
    
    while True:
        if n > r : break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1
    
    return [-1] if len(answer) == 0 else answer