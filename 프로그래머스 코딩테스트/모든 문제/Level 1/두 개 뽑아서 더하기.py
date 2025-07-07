# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))

# 다른 사람 풀이1
def solution1(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

# 다른 사람 풀이2
from itertools import combinations

def solution2(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer