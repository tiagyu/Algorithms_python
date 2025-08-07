# 원하는 문자열 찾기
def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()

    if pat in myString:
        answer = 1
    else:
        answer = 0
    return answer


# 다른 사람 풀이1
def solution1(myString, pat):
    return int(pat.lower() in myString.lower())


# 다른 사람 풀이2
def solution2(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0
