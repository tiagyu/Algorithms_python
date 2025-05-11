def solution(a, b, c, d):
    values = [a, b, c, d]
    count_dict = {}

    # 값 등장 횟수 카운트
    for v in values:
        count_dict[v] = count_dict.get(v, 0) + 1

    # 4개가 모두 같을 경우
    if len(count_dict) == 1:
        p = values[0]
        return 1111 * p

    # 3개 같고 1개 다른 경우 OR 2개씩 같은 경우
    elif len(count_dict) == 2:
        keys = list(count_dict.keys())
        vals = list(count_dict.values())

        if 3 in vals:
            # 3 + 1
            p = keys[vals.index(3)]
            q = keys[vals.index(1)]
            return (10 * p + q) ** 2
        else:
            # 2 + 2
            p, q = keys
            return (p + q) * abs(p - q)

    # 2개 같고 나머지 하나씩 다른 경우
    elif len(count_dict) == 3:
        two_count = None
        one_values = []

        for k, v in count_dict.items():
            if v == 2:
                two_count = k
            elif v == 1:
                one_values.append(k)

        if len(one_values) == 2:
            q, r = one_values
            return q * r

    # 네 개가 전부 다를 경우
    return min(values)
