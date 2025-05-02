def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if all(d in ['0','5'] for d in list(str(i))):
            answer.append(i)
    return answer if len(answer) > 0 else [-1]