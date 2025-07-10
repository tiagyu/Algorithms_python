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