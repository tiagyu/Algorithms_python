# 세 개의 구분자
def solution(myStr):
    mapping = str.maketrans({"a": " ", "b": " ", "c": " "})
    myStr = myStr.translate(mapping)
    if myStr.split():
        return myStr.split()
    else:
        return ["EMPTY"]


# 다른 사람 풀이1
def solution1(myStr):
    answer = [
        x
        for x in myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
        if x
    ]
    return answer if answer else ["EMPTY"]


# 다른 사람 풀이2
import re


def solution2(myStr):
    answer = [m for m in re.split("a|b|c", myStr) if m]
    if len(answer) == 0:
        answer = ["EMPTY"]

    return answer
