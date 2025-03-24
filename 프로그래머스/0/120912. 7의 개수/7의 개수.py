# 7의 개수
def solution(array):
    answer = 0
    for i in array:
        i = str(i)
        i_list = list(i)
        for j in i_list:
            if j == "7":
                answer += 1
    return answer
