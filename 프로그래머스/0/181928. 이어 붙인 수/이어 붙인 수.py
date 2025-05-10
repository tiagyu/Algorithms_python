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