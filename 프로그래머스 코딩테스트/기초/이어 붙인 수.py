# 이어 붙인 수
def solution(num_list):
    odd = ""
    even = ""

    for num in num_list:
        if num % 2:
            odd += str(num)
        else:
            even += str(num)

    answer = int(odd) + int(even)
    return answer

# 다른 사람 풀이1
def solution1(num_list):
    even = int("".join([str(i) for i in num_list if i%2 == 0]))
    odd = int("".join([str(i) for i in num_list if not i%2 == 0]))
    return even + odd