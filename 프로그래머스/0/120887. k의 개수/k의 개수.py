def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        num_list = list(str(num))
        for nl in num_list:
            if nl == str(k):
                answer += 1
    return answer