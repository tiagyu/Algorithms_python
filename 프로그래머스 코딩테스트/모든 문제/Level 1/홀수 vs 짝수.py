# 홀수 vs 짝수
def solution(num_list):
    odd_sum, even_sum = 0,0
    for i in range(len(num_list)):
        if i % 2:
            even_sum += num_list[i]
        else:
            odd_sum += num_list[i]
    answer = max(even_sum, odd_sum)
    return answer

# 다른 사람 풀이1
def solution1(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))

# 다른 사람 풀이2
def solution2(num_list):
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        elif i % 2 == 1 :
            odd += num_list[i]
    if even > odd :
        return even
    else:
        return odd 