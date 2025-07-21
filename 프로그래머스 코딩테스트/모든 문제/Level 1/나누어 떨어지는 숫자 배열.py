# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer):
        return sorted(answer)
    else:
        return [-1]

# 다른 사람 풀이1
def solution1(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]

# 다른 사람 풀이2
def solution2(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        answer = [-1]

    answer.sort()        
    return answer