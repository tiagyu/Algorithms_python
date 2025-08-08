# 소문자로 바꾸기
def solution(myString):
    answer = myString.lower()
    return answer


# 다른 사람 풀이1
def solution1(myString):
    answer = ""
    for i in myString:
        if ord(i) < 95:
            i = ord(i) + 32
            answer += str(chr(i))
        else:
            answer += i

    return answer
