# x 사이의 개수
def solution(myString):
    s = myString.split("x")
    answer = [len(i) for i in s]
    return answer


# 다른 사람 풀이1
def solution1(myString):
    return [len(w) for w in myString.split("x")]


# 다른 사람 풀이2
def solution2(myString):
    answer = []
    myString = myString.split("x")
    for i in myString:
        answer.append(len(i))
    return answer
