# 접미사인지 확인하기
def solution(my_string, is_suffix):
    suffix = []
    list_mystring = list(my_string)

    while len(list_mystring) > 0:
        suffix.append("".join(list_mystring))
        list_mystring.pop(0)
    if is_suffix in suffix:
        return 1
    return 0

# 다른 사람풀이1
def solution1(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix: return 1
    return 0

# 다른 사람풀이2
def solution2(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))