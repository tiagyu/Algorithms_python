# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []
    for num, bol in zip(arr, flag):
        if bol:
            answer += [num] * num * 2
        else:
            for _ in range(num):
                answer.pop()
    return answer


# 다른 사람 풀이1
def solution1(arr, flag):
    arr1 = []
    for i, j in zip(arr, flag):
        if j:
            arr1 += [i] * i * 2
        else:
            arr1 = arr1[:-i]
    return arr1


# 다른 사람 풀이2
def solution2(arr, flag):
    X = []
    for i, f in enumerate(flag):
        if f:
            X += [arr[i]] * (arr[i] * 2)
        else:
            for _ in range(arr[i]):
                X.pop()
    return X
