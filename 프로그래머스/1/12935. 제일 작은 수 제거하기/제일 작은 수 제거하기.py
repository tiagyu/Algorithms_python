def solution(arr):
    if len(arr) > 1:
        arr.remove(sorted(arr)[0])
        return arr
    else:
        return [-1]