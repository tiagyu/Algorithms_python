def solution(my_string, is_prefix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[:i+1])

    if is_prefix in answer:
        return 1
    return 0