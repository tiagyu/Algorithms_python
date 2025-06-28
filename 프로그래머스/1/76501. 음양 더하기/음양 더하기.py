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
