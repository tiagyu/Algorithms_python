def solution(name, yearning, photo):
    name_dict = dict(zip(name, yearning))
    answer = []

    for i in photo:
        cnt = 0
        for j in i:
            if j in name:
                cnt += name_dict[j]
        answer.append(cnt)
    return answer