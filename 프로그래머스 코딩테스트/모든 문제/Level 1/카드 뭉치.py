# 카드 뭉치
def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and i == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

# 다른 사람 풀이1
from collections import deque

def solution1(cards1, cards2, goal):
    card1_q = deque(list(cards1))
    card2_q = deque(list(cards2))

    for target in goal:
        if card1_q and card1_q[0] == target:
            card1_q.popleft()
        elif card2_q and card2_q[0] == target:
            card2_q.popleft()
        else:
            return "No"
    return "Yes"