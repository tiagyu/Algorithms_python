# 진료순서 정하기
def solution(emergency):
    answer = []
    emergency_sort = sorted(emergency,reverse=True)

    for i in emergency:
        for index, num in enumerate(emergency_sort,start=1):
            if i == num:
                answer.append(index)

    return answer

# index를 활용한 풀이
def solution(emergency):
    answer = []
    sort_num = sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(sort_num.index(i)+1)
        
    return answer

# 리스트 전부 비교
def solution3(emergency):
    answer = []
    for i in emergency:
        idx = 1
        for j in emergency:
            if i < j:
                idx += 1
            answer.append(idx)
    return answer