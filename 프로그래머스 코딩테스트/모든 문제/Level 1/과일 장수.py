# 과일 장수
def solution(k, m, score):
    answer = 0
    score = sorted(score,reverse=True)
    for i in range(0,len(score),m):
        box = score[i:i+m]
        if len(box) == m:
            answer += min(box) * m
    return answer

# 다른 사람 풀이1
def solution1(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

# 다른 사람 풀이2
def solution2(k, m, score):
    answer = 0
    score.sort(reverse=True)
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m:
            answer += min(apple) * m
    return answer