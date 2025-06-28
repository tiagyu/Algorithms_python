# 음양 더하기
def solution(absolutes, signs):
    true = True
    false = False
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == false:
            answer -= absolutes[i]
        elif signs[i] == true:
            answer += absolutes[i]
    return answer

# 다른 사람 풀이1
def solution1(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# 다른 사람 풀이2
def solution2(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer