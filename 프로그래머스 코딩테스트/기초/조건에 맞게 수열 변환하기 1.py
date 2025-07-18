# 조건에 맞게 수열 변환하기 1
def solution(arr):
    answer = []
    for i in arr:
        if i % 2 == 0 and i >=50:
            answer.append(int(i/2))
        elif i % 2 != 0 and i < 50:
            answer.append(int(i*2))
        else:
            answer.append(i)
    return answer

# 다른 사람 풀이1
def solution1(arr):
    return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]

# 다른 사람 풀이2
def solution2(arr):
    for i in range(len(arr)):
        x=arr[i]
        if x>=50 and not x%2: arr[i]//=2
        elif x<50 and x%2: arr[i]*=2
    return arr