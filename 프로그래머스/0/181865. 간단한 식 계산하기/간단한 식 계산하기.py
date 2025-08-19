def solution(binomial):
    s = binomial.split(" ")
    a, op, b = s[0], s[1], s[2]

    if op == '+':
        answer = int(a) + int(b)
        return answer
    elif op == "-":
        answer = int(a) - int(b)
        return answer
    else:
        answer = int(a) * int(b)
        return answer