# 다음에 올 숫자
def solution(common):
    # 등비 수열
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        return common[0] + diff * (len(common))
    # 등차 수열열
    else:
        ratio = common[1] / common[0]
        return common[0] * ratio ** (len(common))
    
# 다른 사람 풀이1
def solution1(common):
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1] + (b-a)
    else:
        return common[-1] * (b//a)