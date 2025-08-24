# 문자열 바꿔서 찾기
def solution(myString, pat):
    mapping = str.maketrans({"A": "B", "B": "A"})
    myString = myString.translate(mapping)

    if pat in myString:
        return 1
    else:
        return 0


# 다른 사람 풀이1
def solution1(myString, pat):
    return int(pat in myString.replace("A", "C").replace("B", "A").replace("C", "B"))


# 다른 사람 풀이2
def solution2(myString, pat):
    return int("".join(["A" if i == "B" else "B" for i in pat]) in myString)
