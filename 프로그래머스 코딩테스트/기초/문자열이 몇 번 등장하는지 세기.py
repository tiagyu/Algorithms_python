# 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    count = 0

    for i in range(0, len(myString) - len(pat) + 1):
        print(myString[i : i + len(pat)])
        if myString[i : i + len(pat)] == pat:
            count += 1
    return count


# 다른 사람 풀이1
def solution1(myString, pat):
    answer = 0
    for i, x in enumerate(myString):
        if myString[i:].startswith(pat):
            answer += 1
    return answer


# 다른 사람 풀이2
def solution2(myString, pat):
    return sum(myString[i : i + len(pat)] == pat for i in range(len(myString)))
