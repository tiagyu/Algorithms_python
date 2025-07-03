def solution(number, limit, power):
    num_list = [1]
    for i in range(2,number+1):
        count = 0
        j = 1
        while j * j <= i:
            if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1
            j += 1
        if count > limit:
            count = power
        num_list.append(count)
    answer = sum(num_list)
    return answer