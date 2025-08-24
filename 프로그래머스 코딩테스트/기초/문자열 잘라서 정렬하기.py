# 문자열 잘라서 정렬하기
def solution(myString):
    answer = [w for w in myString.split("x") if w.isalpha()]
    return sorted(answer)


# 다른 사람 풀이 1
def solution1(myString):
    return sorted(ch for ch in myString.split("x") if ch)


# 다른 사람 풀이 2
def solution2(myString):
    answer = " ".join(myString.split("x")).split()
    return sorted(answer)
