# 006 연속된 자연수의 합 구하기
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index !=n :
    if sum == n: # 정답 케이스
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else: # sum < n
        end_index += 1
        sum += end_index

print(count)