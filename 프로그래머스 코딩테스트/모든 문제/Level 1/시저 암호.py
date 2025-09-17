# 시저 암호
def solution(s, n):
    answer = []
    for i in s:
        if ord(i) == 32:
            answer.append(i)
        else:
            if i.islower():
                answer.append(chr((ord(i) - 97 + n) % 26 + 97))
            else:
                answer.append(chr((ord(i) - 65 + n) % 26 + 65))
    return "".join(answer)


# 다른 사람 풀이1
def solution1(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))

    return "".join(s)


# 다른 사람 풀이2
def solution2(s, n):
    answer = ""
    for i in s:
        if i:
            if i >= "A" and i <= "Z":
                answer += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
            elif i >= "a" and i <= "z":
                answer += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
            else:
                answer += " "
    return answer
