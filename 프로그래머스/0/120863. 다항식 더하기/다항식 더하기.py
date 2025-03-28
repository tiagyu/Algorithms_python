# 다항식 더하기
def solution(polynomial):
    x_value = 0
    num_value = 0
    polynomial_split = polynomial.split(" ")

    for i in range(0,len(polynomial_split),2):
        # x값
        if polynomial_split[i].find("x") != -1:
            # x값만 있는지 확인
            if polynomial_split[i] != "x":
                x_value += int(polynomial_split[i][:-1])
            else:
                x_value += 1
        # 상수값
        else:
            num_value += int(polynomial_split[i])
            
    if x_value == 0:
        answer = f"{num_value}"
    elif num_value == 0:
        if x_value > 1:
            answer = f"{x_value}x"
        else:
            answer = f"x"
    elif x_value == 1:
        answer = f"x + {num_value}"
    else:
        answer = f"{x_value}x + {num_value}"
        
    return answer