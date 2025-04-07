# 등수 매기기
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

# 다른 사람 풀이1
def solution1(score):
    a = sorted([sum(i) for i in score], reverse=True)
    return [a.index(sum(i)) + 1 for i in score]

# 다른 사람 풀이2
def solution2(score):
    rank = sorted([sum(s)/2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s)/2] for s in score]