# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    num = ""
    answer = 0

    for i in list(my_string):
        if i.isdigit():
            num += i
        else:
            if len(num) > 0:
                answer += int(num)
                num = ""
    
    if len(num) > 0:
        answer += int(num)
                
    return answer