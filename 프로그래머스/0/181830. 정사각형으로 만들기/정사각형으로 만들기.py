def solution(arr):
    if len(arr) != len(arr[0]):
        # 행이 열보다 숫자가 큰 경우
        if len(arr) > len(arr[0]):
            while len(arr) > len(arr[0]):
                for i in range(len(arr)):
                    arr[i].append(0)
        # 열이 행보다 숫자가 큰 경우
        if len(arr) < len(arr[0]):
            while len(arr) < len(arr[0]):
                arr.append([0] * len(arr[0]))
        return arr
    return arr