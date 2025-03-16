# 인덱스 바꾸기
def solution(my_string, num1, num2):
    list_my_string = list(my_string)

    list_my_string_num1 = list_my_string[num1]
    list_my_string_num2 = list_my_string[num2]

    list_my_string[num1] = list_my_string_num2
    list_my_string[num2] = list_my_string_num1

    answer = "".join(list_my_string)

    return answer

# 다른 사람 풀이 1
def solution1(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return "".join(s)
