# OX퀴즈
def solution(quiz):
    answer = []
    for modification in quiz:
        modification_split = modification.split(" ")
        if modification_split[1] == "+":
            value = int(modification_split[0]) + int(modification_split[2])
            if value == int(modification_split[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            value = int(modification_split[0]) - int(modification_split[2])
            if value == int(modification_split[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer

# 다른 사람 풀이1
def solution1(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(" = ")
        a, op, b = L.split()
        if op == "+":
            result = 'O' if int(a) + int(b) == int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a) - int(b) == int(R) else 'X'
            answer.append(result)
    return answer

# 다른 사람 풀이2
def solution2(quiz):
    answer = []
    for i in quiz:
        i = i.replace("=","==")
        answer.append("o" if eval(i) else "X")
    return answer