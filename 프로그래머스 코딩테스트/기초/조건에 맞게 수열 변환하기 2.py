# 조건에 맞게 수열 변환하기 2
def solution(arr):
    x = 0
    while True:
        prev_arr = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
        if arr == prev_arr:
            break
        x += 1
    return x


# 다른 사람 풀이1
def solution1(arr):
    answer = 0
    old = arr
    while True:
        new = []
        for i in old:
            if i >= 50 and i % 2 == 0:
                new.append(i // 2)
            elif i < 50 and i % 2 == 1:
                i = i * 2 + 1
            new.append(int(i))
        if old == new:
            break
        else:
            old = new
            answer += 1
    return answer


# 다른 사람 풀이2
def solution2(arr):
    answer = 0

    while True:
        arr_trans = []

        for i in arr:
            if i >= 50 and i % 2 == 0:
                arr_trans.append(i // 2)
            elif i < 50 and i % 2 == 1:
                arr_trans.append(i * 2 + 1)
            else:
                arr_trans.append(i)

        if arr == arr_trans:
            return answer

        answer += 1
        arr = arr_trans
