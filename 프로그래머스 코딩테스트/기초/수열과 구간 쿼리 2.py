# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    for query in queries:
        s,e,k = query[0],query[1],query[2]
        arr_list = []
        for i in range(s,e+1):
            if arr[i] > k:
                arr_list.append(arr[i])    
        
        if len(arr_list) == 0:
            answer.append(-1)
        else:
            answer.append(min(arr_list))
    return answer

# 다른 사람 풀이1
def solution1(arr, queries):
    answer = []
    for s,e,k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

# 다른 사람 풀이2
def solution2(arr, queries):
    answer = []
    for s,e,k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(i) == 0 else min(l))
    return answer