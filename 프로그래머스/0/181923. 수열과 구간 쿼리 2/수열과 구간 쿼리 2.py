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