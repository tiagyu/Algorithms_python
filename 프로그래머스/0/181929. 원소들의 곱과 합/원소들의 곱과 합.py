def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    if answer < sum(num_list)**2:
        return 1
    return 0