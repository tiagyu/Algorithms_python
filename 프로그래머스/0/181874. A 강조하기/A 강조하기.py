def solution(myString):
    answer = ""
    myString = myString.lower()
    for s in list(myString):
        if s == "a":
            answer += s.upper()
        else:
            answer += s
    return answer
