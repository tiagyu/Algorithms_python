# 2161 : 카드 1
from collections import deque

N = int(input())

# 리스트 생성
queue = deque(range(1,N+1))

answer = []

while len(queue) > 1:
    # 맨 앞의 카드 버림
    answer.append(queue.popleft())
    # 그 다음 카드 맨 뒤로 이동
    queue.append(queue.popleft())

# 마지막 카드 반영
answer.append(queue.popleft())

print(answer)