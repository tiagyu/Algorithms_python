# 5명씩
def solution(names):
    answer = answer = [names[i] for i in range(0,len(names),5)]
    return answer

# 다른 사람 풀이1
def solution1(names):
    return names[::5]