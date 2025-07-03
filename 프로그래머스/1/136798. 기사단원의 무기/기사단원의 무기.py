def solution(number, limit, power):
    num_list = [1]
    for i in range(2,number+1):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if j * j == i:
                count += 1
            elif i % j == 0:
                count += 2
        if count > limit:
            count = power
        num_list.append(count)
    answer = sum(num_list)
    return answer