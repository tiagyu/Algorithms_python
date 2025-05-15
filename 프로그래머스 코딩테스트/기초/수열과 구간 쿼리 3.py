# 수열과 구간 쿼리 3
def solution(arr, queries):
    for query in queries:
        arr[query[0]], arr[query[1]] = arr[query[1]], arr[query[0]]
    return arr

# 다른 사람 풀이1
def solution1(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr