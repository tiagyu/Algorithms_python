# 크기가 작은 부분 문자열
def solution(t, p):
    n = len(p)
    answer = 0
    sep = []
    
    for i in range(len(t) - n+1 ):
            sep.append(t[i:i+n])
    
    for j in sep:
        if int(j) <= int(p):
            answer += 1
        
    return answer

print('solution',solution("3141592","271"))


# for 문에서 바로 해결
def solution1(t,p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1
    
    return answer

print('solution1',solution1("10203","15"))