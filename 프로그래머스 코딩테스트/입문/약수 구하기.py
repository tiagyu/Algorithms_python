# 약수 구하기
def solution(n):
    answer = [aliquit for aliquit in range(1, n+1) if n % aliquit == 0]
    return answer

# 다른 사람들 풀이
def solution1(n):
    answer = []
    k = int(n ** 0.5)
    print(k)
    
    for i in range(1, k+1):
        if n % i == 0:
            answer.append(i)
            answer.append(n // i)
            
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer