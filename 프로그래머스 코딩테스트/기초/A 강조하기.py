# A 강조하기
def solution(myString):
    answer = ""
    myString = myString.lower()
    for s in list(myString):
        if s == "a":
            answer += s.upper()
        else:
            answer += s
    return answer


# 다른 사람 풀이1
def solution1(myString):
    return myString.lower().replace("a", "A")


# 다른 사람 풀이2
def solution2(myString):
    answer = ""
    answer = myString.lower()
    answer = answer.replace("a", "A")
    return answer
