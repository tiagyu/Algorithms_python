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

# 다른 사람 풀이1
def solution1(array):
    return str(array).count("7")

# 다른 사람 풀이2
def solution2(array):
    return "".join(map(str,array)).count("7")