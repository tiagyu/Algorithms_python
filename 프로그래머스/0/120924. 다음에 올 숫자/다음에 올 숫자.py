def solution(common):
    # 등비 수열
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        return common[0] + diff * (len(common))
    # 등차 수열열
    else:
        ratio = common[1] / common[0]
        return common[0] * ratio ** (len(common))