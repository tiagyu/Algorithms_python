# 기사단원의 무기
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

# 다른 사람 풀이1
def cf(n):
    a = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))

def solution1(number, limit, power):
    return sum([cf(i) if cf(i) <= limit else power for i in range(1, number+1)])

# 다른 사람 풀이2
def solution2(number, limit, power):
    sum = []
    for j in range(1, number+1):
        cnt = 0
        for i in range(1, int(j**0.5)+1):
            if (j == i**2):
                cnt += 1
            elif (j % i == 0):
                cnt += 2
        sum.append(cnt)
    res = [i if i <= limit else power for i in sum]
    return res