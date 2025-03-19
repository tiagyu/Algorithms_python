# 가장 큰 수 찾기
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer

# 다른 사람 풀이 1
def solution1(array):
    answer = [0, 0]
    num = array[0]
    for i in range(len(array)):
        if num < array[i]:
            num = array[i]
            answer[0] = num
            answer[1] = i
    return answer