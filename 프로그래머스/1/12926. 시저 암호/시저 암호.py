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