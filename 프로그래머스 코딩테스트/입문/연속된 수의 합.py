# 연속된 수의 합
def solution(num, total):
    answer = []
    start = (total - (num * (num - 1)) // 2) // num
    answer = [start + i for i in range(num)]
    return answer

# 다른 사람 풀이1
def solution1(num, total):
    answer = []
    var = sum(range(num + 1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer