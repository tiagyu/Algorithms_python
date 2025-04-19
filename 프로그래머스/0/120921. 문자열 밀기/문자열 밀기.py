def solution(A, B):
    a_list = list(A)
    answer = 0

    for _ in range(len(A)):
        if "".join(a_list) == B:
            return answer
        last = a_list.pop()
        a_list.insert(0, last)
        answer += 1
    return -1