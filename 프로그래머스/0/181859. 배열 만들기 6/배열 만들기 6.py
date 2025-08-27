def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            answer.pop()
        else:
            answer.append(arr[i])
    if not answer:
        return [-1]
    return answer