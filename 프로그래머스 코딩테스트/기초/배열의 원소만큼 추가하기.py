# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)

    return answer


# 다른 사람 풀이1
def solution1(arr):
    return [i for i in arr for j in range(i)]


# 다른 사람 풀이2
def solution2(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer
