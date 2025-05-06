# 전국 대회 선발 고사
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

# 다른 사람 풀이1
def solution1(rank, attendance):
    arr = sorted([(x, i) for i,x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]

# 다른 사람 풀이2
def solution2(rank, attendance):
    selected = []
    for i,attend in enumerate(attendance):
        if attend:
            selected.append((rank[i], i))
    selected.sort()
    a,b,c = selected[:3]
    return 10000 * a[1] + 100 * b[1] + c[1]