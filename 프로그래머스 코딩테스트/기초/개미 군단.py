# 개미 군단
def solution(hp):
    general_ants = hp // 5
    hp %= 5
    soldier_ants = hp // 3
    hp %= 3
    worker_ants = hp
    answer = general_ants + soldier_ants + worker_ants
    return answer

def solution2(hp):
    answer = 0
    for i in [5,3,1]:
        d, hp = divmod(hp, i)
        answer += d
    return answer
    
print(solution(23))