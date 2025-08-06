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