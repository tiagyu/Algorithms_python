# 1로 만들기
def solution(num_list):
    cnt = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num /= 2
                cnt += 1
            else:
                num = (num-1)/2
                cnt += 1
    return cnt

# 다른 사람 풀이1
def solution1(num_list):
    answer = 0

    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1

    return answer

# 다른 사람 풀이2
def solution2(num_list):
    answer = 0
    for n in num_list:
        while n!=1:
            answer+=1
            if n%2: n=(n-1)//2
            else: n//=2
    return answer