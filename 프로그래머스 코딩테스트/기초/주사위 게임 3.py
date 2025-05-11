# 주사위 게임 3
def solution(a, b, c, d):
    answer = 0
    return answer

a, b, c, d = 4,1,4,4
values = [a, b, c, d]
count_dict= {}

for v in values:
    count_dict[v] = count_dict.get(v,0) + 1

for v, c in count_dict.items():
    # 4개가 같은 경우 -> 1111 × p
    if len(count_dict) == 1:
        print(1111 * v)

    # 3개가 같은 경우 -> (10 × p + q)**2
    elif len(count_dict) == 2:
        if c == 3:
            p = v
        if c == 1:
            q = v
        print((10 * p + q)**2)

# 하나도 같지 않은 경우 -> 최소 값
# 2개가 같은 경우1 -> 2개씩 같은 값 -> (p + q) × |p - q|

# 2개가 같은 경우2 -> q × r