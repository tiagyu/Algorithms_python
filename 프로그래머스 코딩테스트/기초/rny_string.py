# rny_string
def solution(rny_string):
    return rny_string.replace("m", "rn")


# 다른 사람 풀이1
def solution1(rny_string):
    answer = []
    for x in rny_string:
        if x == "m":
            answer.append("rn")
        else:
            answer.append(x)
    return "".join(answer)


# 다른 사람 풀이2
def solution(rny_string):
    answer = ""
    for i in rny_string:
        if i == "m":
            answer += "rn"
        else:
            answer += i
    return answer
