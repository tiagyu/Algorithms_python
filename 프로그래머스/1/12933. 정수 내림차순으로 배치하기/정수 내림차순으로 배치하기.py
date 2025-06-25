def solution(n):
    answer = "".join(reversed(sorted(str(n))))
    return int(answer)