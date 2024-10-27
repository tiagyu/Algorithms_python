def solution(arr):
    answer = []
    array_list = arr
    answer.append(array_list[0])

    # 1. 범위 설정
    for i in range(1,len(arr)):
        if array_list[i] != answer[-1]:
            answer.append(array_list[i])
        
    return answer