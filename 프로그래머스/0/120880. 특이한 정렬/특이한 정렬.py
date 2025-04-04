# 특이한 정렬
def solution(numlist, n):
    dict = {}
    answer= []
    for num in numlist:
        dict[num] = abs(n - num)

    sorted_dict = sorted(dict.items(), key=lambda item : (item[1], -item[0]))

    for i in sorted_dict:
        answer.append(i[0])
    return answer