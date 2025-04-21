def solution(num, total):
    answer = []
    start = (total - (num * (num - 1)) // 2) // num
    answer = [start + i for i in range(num)]
    return answer