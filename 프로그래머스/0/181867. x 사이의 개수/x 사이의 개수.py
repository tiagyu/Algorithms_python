def solution(myString):
    s = myString.split("x")
    answer = [len(i) for i in s]
    return answer