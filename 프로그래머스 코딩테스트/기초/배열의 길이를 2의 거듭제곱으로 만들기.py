# 배열의 길이를 2의 거듭제곱으로 만들기
def solution(arr):
    i = 0
    while 2**i < len(arr):
        i += 1
    arr += [0] * (2**i - len(arr))
    return arr


# 다른 사람 풀이1
def solution1(arr):
    a = 1
    b = len(arr)
    while a < b:
        a *= 2
    return arr + [0] * (a - b)


# 다른 사람 풀이2
def solution2(arr):
    answer = [2**i for i in range(11)]
    while len(arr) not in answer:
        arr.append(0)
    return arr
