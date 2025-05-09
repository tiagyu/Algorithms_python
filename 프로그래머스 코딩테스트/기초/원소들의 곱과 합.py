# 원소들의 곱과 합
def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    if answer < sum(num_list)**2:
        return 1
    return 0

# 다른 사람들 풀이1
def solution1(num_list):
    s = sum(num_list) ** 2
    m = eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0

# 다른 사람들 풀이2
def solution2(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if a<b*b: return 1
    return 0