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

# 다른 사람 풀이 1
def solution1(my_string):
    s = "".join(i if i.isdigit() else " " for i in my_string)
    return sum(int(i) for i in s.split())