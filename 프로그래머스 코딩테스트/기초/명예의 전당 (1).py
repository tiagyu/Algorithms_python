# 명예의 전당 (1)
def solution(k, score):
    answer = []
    honor = []

    for s in score:
        honor.append(s)
        honor.sort()
        if len(honor) > k:
            honor.pop(0)
        answer.append(min(honor))
    return answer

# 다른 사람 풀이1
def solution1(k, score):
    q = []
    answer = []
    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))
    return answer

# 다른 사람 풀이2
import heapq

def solution2(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer