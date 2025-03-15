# 영어가 싫어요
def solution(numbers):
    number_dict = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
    }
    answer = numbers
    for key, value in number_dict.items():
        if key in answer:
            answer  = answer.replace(key, str(value))

    return int(answer)

# 다른 사람 풀이 1
def solution1(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

# 다른 사람 풀이 2
def solution2(numbers):
    number_dict = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
    }
    for k in number_dict.keys():
        numbers = numbers.replace(k, str(number_dict[k]))
    
    return int(numbers)