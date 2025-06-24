# 모의고사
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

# 다른 사람 풀이1
def solution1(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# 다른 사람 풀이2
def solution2(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]