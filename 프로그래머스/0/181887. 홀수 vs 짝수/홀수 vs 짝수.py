def solution(num_list):
    odd_sum, even_sum = 0,0
    for i in range(len(num_list)):
        if i % 2:
            even_sum += num_list[i]
        else:
            odd_sum += num_list[i]
    answer = max(even_sum, odd_sum)
    return answer