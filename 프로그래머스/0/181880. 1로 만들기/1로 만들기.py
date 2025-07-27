def solution(num_list):
    cnt = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num /= 2
                cnt += 1
            else:
                num = (num-1)/2
                cnt += 1
    return cnt