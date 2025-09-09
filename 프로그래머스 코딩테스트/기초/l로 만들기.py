# l로 만들기
def solution(myString):
    answer = ""
    for i in myString:
        if ord(i) < ord("l"):
            answer += "l"
        else:
            answer += i
    return answer


# 다른 사람 풀이1
def solution1(myString):
    answer = [x if x > "l" else "l" for x in myString]
    return "".join(answer)


# 다른 사람 풀이2
def solution2(myString):
    answer = ""
    for i in myString:
        if i < "l":
            answer += "l"
        else:
            answer += i
    return answer
