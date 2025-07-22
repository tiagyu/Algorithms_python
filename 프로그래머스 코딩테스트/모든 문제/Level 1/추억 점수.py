# 추억 점수
def solution(name, yearning, photo):
    name_dict = dict(zip(name, yearning))
    answer = []

    for i in photo:
        cnt = 0
        for j in i:
            if j in name:
                cnt += name_dict[j]
        answer.append(cnt)
    return answer

# 다른 사람 풀이1
def solution1(name, yearning, photo):
    n = len(name)
    dct = {}
    for i in range(n):
        dct[name[i]] = yearning[i]
    
    answer = []
    for lst in photo:
        cnt = 0
        for a in lst:
            if a in dct:
                cnt += dct[a]
    answer.append(cnt)
    return answer

# 다른 사람 풀이2
def solution2(name, yearning, photo):
    answer = []
    
    for i in photo:
        score = 0
        for j in range(len(name)):
            if name[j] in i:
                score+=yearning[j]
    answer.append(score)
    return answer