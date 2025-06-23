# 푸드 파이트 대회
def solution(food):
    answer = ""
    for i in range(1,len(food)):
        n = food[i] // 2
        answer += str(i) * n
    return answer + '0' +answer[::-1]

# 다른 사람 풀이1
def solution1(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer

# 다른 사람 풀이2
def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]