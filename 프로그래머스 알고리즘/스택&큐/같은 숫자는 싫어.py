# 같은 숫자는 싫어
# solution 1
def solution(arr):
    answer = []
    array_list = arr
    answer.append(array_list[0])

    # 1. 범위 설정
    for i in range(1,len(arr)):
        if array_list[i] != answer[-1]:
            answer.append(array_list[i])
        
    return answer

print(solution([1,1,3,3,0,1,1]))

# solution 2
def solution2(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or answer[-1] != a:
            answer.append(a)
    return answer

print(solution2([1,1,3,3,0,1,1]))
