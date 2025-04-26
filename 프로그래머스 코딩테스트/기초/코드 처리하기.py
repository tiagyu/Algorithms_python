# 코드 처리하기
def solution(code):
    mode = 0
    answer = ""

    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
                pass
            else:
                if i % 2 == 0:
                    answer += code[i]
        else:
            if code[i] == "1":
                mode = 0
                pass
            else:
                if i % 2 != 0:
                    answer += code[i]
    if len(answer) == 0:
        return 'EMPTY'
    return answer

# 다른 사람풀이1
def solution1(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

# 다른 사람풀이2
def solution2(code):
    answer = ""
    mode = 0
    
    for i in range(len(code)):
        if code[i] == "1":
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]
    return answer if answer else "EMPTY"