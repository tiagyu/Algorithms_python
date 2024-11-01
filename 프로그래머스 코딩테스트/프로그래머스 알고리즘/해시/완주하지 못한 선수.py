# 완주하지 못한 선수
# 1. Sorting Loop을 활용한 문제 해결
def solution1(participant, completion):
    # 1. 두 리스트를 sort 한다
    participant.sort()
    completion.sort()
    
    # 2. completion list의 length 만큼 돌면서, particpants에 존재하지 않는 선수를 찾는다
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수다
    return participant[len(participant)-1]

print('Sol 1 :',solution1(["leo", "kiki", "eden"],["eden", "kiki"]))

# 2. Hash를 활용한 Solution
def solution2(participant, completion):
    hasDict = {}
    sumHash = 0
    
    # 1. participant list의 hash를 구하고, hash 값을 더한다.
    for part in participant:
        hasDict[hash(part)] = part
        sumHash += hash(part)
        
    # 2. completion list에 hash를 빼준다.
    for comp in completion:
        sumHash -= hash(comp)
    
    # 3. 남은 값이 완주하지 못한 선수의 hash 값이 된다.
    return hasDict[sumHash]

print('Sol 2 :',solution2(["leo", "kiki", "eden"],["eden", "kiki"]))

# 3. Counter를 활용한 Solution
from collections import Counter

def solution3(participant, completion):
    # 1. participants의 counter를 구한다
    part_counter = Counter(participant)
    
    # 2. completion의 counter를 구한다
    comp_counter = Counter(completion)
    
    # 3. 둘의 차를 구하고, key를 읽어온다
    answer = part_counter - comp_counter
    return list(answer.keys())[0]

print('Sol 3 :',solution3(["leo", "kiki", "eden"],["eden", "kiki"]))