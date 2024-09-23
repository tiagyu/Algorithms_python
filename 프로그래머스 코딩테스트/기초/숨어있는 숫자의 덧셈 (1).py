# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    numb = '123456789'
    answer = 0
    for i in numb:
        if i in my_string:
            answer += int(i) * my_string.count(i)
    return answer

def solution2(my_string):
    answer = 0
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass
    return answer

def solution3(my_string):
    answer = 0
    number = ['1','2','3','4','5','6','7','8','9']
    for i in range(len(my_string)):
        if my_string[i] in number:
            answer += int(my_string[i])
        else:
            continue
    return answer

print(solution3("1a2b3c4d123"))