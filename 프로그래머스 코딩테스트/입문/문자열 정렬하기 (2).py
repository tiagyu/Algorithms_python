# 문자열 정렬하기 (2)
def solution(my_string):
    my_string = my_string.lower()
    my_string = sorted(my_string)
    answer = "".join(my_string)
    return answer

# 다른 사람 풀이1
def solution1(my_string):
    return "".join(sorted(my_string.lower()))

# 다른 사람 풀이2
def solution2(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer.append(chr(ord(i)+32))
        else:
            answer.append(i)
    return "".join(sorted(answer))