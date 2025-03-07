# 합성수 찾기
def solution(n):
    answer = 0
    divded_answer = []
    
    # 소수 구하기
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i >= j and i % j == 0:
                divded_answer.append(i)
        if len(divded_answer) <= 2:
            answer += 1
        divded_answer = []
    return int(n - answer)

# 다른 사람 풀이 1
def solution2(n):
    output = 0
    for i in range(4, n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

# 다른 사람 풀이 2
def solution3(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    return answer