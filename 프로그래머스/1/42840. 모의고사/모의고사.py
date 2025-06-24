def solution(answers):
    answer = []
    p1 = [i for i in range(1,6)]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    n = (len(answers) // len(p1)) + 1
    p1 = p1 * n
    p2 = p2 * n
    p3 = p3 * n

    p1_count = sum([a==b for a,b in zip(p1[:len(answers)],answers)])
    p2_count = sum([a==b for a,b in zip(p2[:len(answers)],answers)])
    p3_count = sum([a==b for a,b in zip(p3[:len(answers)],answers)])

    answers_dict = {1:p1_count, 2:p2_count, 3:p3_count}
    max_num = max(p1_count, p2_count, p3_count)
    for k,v in answers_dict.items():
        if max_num == v:
            answer.append(k)
    return answer
