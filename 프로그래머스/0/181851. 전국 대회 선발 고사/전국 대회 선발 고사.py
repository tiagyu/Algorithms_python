def solution(rank, attendance):
    emtpy_dict = {}
    answer = []
    for i, index in enumerate(range(len(rank))):
        emtpy_dict[rank[i]] = attendance[i], index

    sort_dict = sorted(emtpy_dict.items(), key=lambda x : x[0])

    for value in sort_dict:
        if value[1][0]:
            answer.append(value[1][1])
        if len(answer) > 2:
            break

    return 10000 * answer[0] + 100 * answer[1] + answer[2]