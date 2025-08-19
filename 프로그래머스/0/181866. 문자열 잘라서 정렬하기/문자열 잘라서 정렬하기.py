def solution(myString):
    answer = [w for w in myString.split("x") if w.isalpha()]
    return sorted(answer)