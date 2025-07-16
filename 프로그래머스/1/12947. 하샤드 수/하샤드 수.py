def solution(x):
    num = sum(map(int, list(str(x))))

    if x % num:
        return False
    else:
        return True