def solution(num):
    i = 0
    if num != 1:
        while num != 1 and i <= 500:
            i += 1
            if num % 2 == 0:
                num /= 2
            else:
                num = (num * 3) + 1
        if i > 500:
            return -1
        else:
            return i
    else:
        return 0