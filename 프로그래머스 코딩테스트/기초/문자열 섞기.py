# 문자열 섞기
def solution(str1, str2):
    answer = ''
    str1_list = list(str1)
    str2_list = list(str2)

    for i in range(len(str1)):
        answer += str1_list[i]
        answer += str2_list[i]
    return answer

# 다른 사람 풀이1
def solution1(str1, str2):
    answer = "".join(str1[i] + str2[i] for i in range(len(str1)))
    return answer

# 다른 사람 풀이2
def solution2(str1, str2):
    answer = ""
    for s1, s2 in zip(str1, str2):
        answer += s1 + s2
    return answer