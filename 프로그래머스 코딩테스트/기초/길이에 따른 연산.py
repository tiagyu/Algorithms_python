# 길이에 따른 연산
def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for num in num_list:
            answer *= num
    return answer

# 다른 사람 풀이1
def solution1(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))