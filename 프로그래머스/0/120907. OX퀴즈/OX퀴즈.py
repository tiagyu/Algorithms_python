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

        