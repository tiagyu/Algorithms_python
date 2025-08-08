# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    for i in range(len(strArr)):
        if i % 2:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    return strArr


# 다른 사람 풀이1
def solution1(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]


# 다른 사람 풀이2
def solution2(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer
