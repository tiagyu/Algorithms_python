# ad 제거하기
def solution(strArr):
    answer = [s for s in strArr if "ad" not in s]
    return answer


# 다른 사람 풀이1
def solution1(strArr):
    answer = []
    for x in strArr:
        if "ad" in x:
            continue
        answer.append(x)
    return answer


# 다른 사람 풀이2
def solution2(strArr):
    answer = []
    for i in strArr:
        if "ad" not in i:
            answer.append(i)

    return answer
