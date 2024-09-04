# 머쓱이보다 키 큰 사람
def solution(array, height):
    array.sort(reverse=True)
    answer_list = []
    for i in array:
        if i > height:
            answer_list.append(i)
    answer = len(answer_list)
    return answer

print(solution([149, 180, 192, 170],167))
