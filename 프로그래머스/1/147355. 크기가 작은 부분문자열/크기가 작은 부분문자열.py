def solution(t, p):
    n = len(p)
    answer = 0
    sep = []
    
    for i in range(len(t) - n+1 ):
            sep.append(t[i:i+n])
    
    for j in sep:
        if int(j) <= int(p):
            print(j)
            answer += 1
        
    return answer