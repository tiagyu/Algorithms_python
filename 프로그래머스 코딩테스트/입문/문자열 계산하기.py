# 문자열 계산하기
def solution(my_string):
    my_string_split = my_string.split(" ")
    answer = int(my_string_split[0])
    
    for i in range(len(my_string_split)):
        if my_string_split[i] == "+":
            answer += int(my_string_split[i+1])
        elif my_string_split[i] == "-":
            answer -= int(my_string_split[i+1])
        else:
            pass
    return answer

# 다른 사람 풀이1
def solution1(my_string):
    return sum(int(i) for i in my_string.replace(" - ", " + -").split(" + "))

# 다른 사람 풀이2
def solution2(my_string):
    answer = eval(my_string)
    return answer