# 정수 내림차순으로 배치하기
def solution(n):
    answer = "".join(reversed(sorted(str(n))))
    return int(answer)