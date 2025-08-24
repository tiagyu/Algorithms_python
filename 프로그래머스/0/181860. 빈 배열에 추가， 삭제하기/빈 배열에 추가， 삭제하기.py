def solution(arr, flag):
    answer = []
    for num, bol in zip(arr, flag):
        if bol:
            answer += [num] * num * 2
        else:
            for _ in range(num):
                answer.pop()
    return answer