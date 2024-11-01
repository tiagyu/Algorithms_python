from collections import deque

def solution(priorities, location):
    # deque에 리스트 넣기 -> pop 효율적 연산을 위함
    prior = deque(priorities)
    answer = []
    
    # while len(prior) > 0:
    for i in list(prior):
        m = max(prior)
        print(i,m)
        if i != m:
            prior.append(i)
            prior.popleft()
        else:
            answer.append(i)
            prior.popleft()
    print(answer)
    return 

print(solution([2, 1, 3, 2],2))