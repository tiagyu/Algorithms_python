# 최댓값 만들기 (2)

def solution(numbers):
    numbers.sort()
    n = len(numbers)
    number_1 = numbers[0] * numbers[1]
    number_2 = numbers[n-1] * numbers[n-2]
    if number_1 > number_2:
        return number_1
    else:
        return number_2

def solution2(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])