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
    
    # 출력 케이스
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

# 다른 사람 풀이1
def solution1(polynomial):
    xnum = 0
    const = 0
    
    for c in polynomial.split(" + "):
        if c.isdigit():
            const += int(c)
        else:
            xnum = xnum + 1 if c == "x" else xnum+int(c[:-1])
    
    if xnum == 0:
        return str(const)
    elif xnum == 1:
        return 'x + ' + str(const) if const != 0 else 'x'
    else:
        return f'{xnum}x + {const}' if const != 0 else f'{xnum}x'