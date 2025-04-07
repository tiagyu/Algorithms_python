def solution(score):
    average_score = [(index, sum(pair)/2) for index, pair in enumerate(score)]
    sort_average_score = sorted(average_score, key=lambda x: -x[1])

    rank_dict = {}
    rank = 1
    prev_score = None
    count = 0

    for idx,avg in sort_average_score:
        if avg != prev_score:
            rank = count + 1
            prev_score = avg
        rank_dict[idx] = rank
        count += 1

    answer = [rank_dict[i] for i in range(len(score))]
    return answer