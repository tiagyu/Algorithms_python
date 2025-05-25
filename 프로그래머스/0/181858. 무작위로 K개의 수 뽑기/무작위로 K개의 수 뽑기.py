def solution(arr, k):
    answer = []
    for num in arr:
        if len(answer) < k and not num in answer:
            answer.append(num)

    while len(answer) < k:
        answer.append(-1)
    return answer