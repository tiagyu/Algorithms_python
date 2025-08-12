# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    if alp in my_string:
        my_string = my_string.replace(alp, alp.upper())
        return my_string
    else:
        return my_string

# 다른 사람 풀이1
def solution1(my_string, alp):
    return my_string.replace(alp, alp.upper())

# 다른 사람 풀이2
def solution2(my_string, alp):
    result = ""
    for c in my_string:
        if c == alp:
            result += c.upper()
        else:
            result += c
    return result