# 배열 조각하기
def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

# 다른 사람 풀이1
def solution1(arr, query):
    for k,q in enumerate(query):
        if k % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr