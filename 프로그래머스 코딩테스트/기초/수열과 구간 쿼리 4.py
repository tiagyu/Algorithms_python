# 수열과 구간 쿼리 4
def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if i:
                if i % k == 0:
                    arr[i] += 1
            else:
                arr[i] += 1
    return arr
