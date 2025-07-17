def solution(numbers):
    all_num = [i for i in range(0,10)]

    diff = set(all_num) - set(sorted(numbers))
    return sum(diff)