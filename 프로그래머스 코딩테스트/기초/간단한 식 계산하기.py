# 간단한 식 계산하기
def solution(binomial):
    s = binomial.split(" ")
    a, op, b = s[0], s[1], s[2]

    if op == "+":
        answer = int(a) + int(b)
        return answer
    elif op == "-":
        answer = int(a) - int(b)
        return answer
    else:
        answer = int(a) * int(b)
        return answer


# 다른 사람 풀이1
def solution(binomial):
    a, op, b = binomial.split()

    a = int(a)
    b = int(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b

    return result


# 다른 사람 풀이2
def solution2(binomial):
    return eval(binomial)
