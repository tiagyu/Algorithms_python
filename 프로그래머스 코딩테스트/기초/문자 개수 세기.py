# 문자 개수 세기
def solution(my_string):
    answer = [0 for _ in range(26*2)]
    high_alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}
    low_alphabet_dict = {chr(i): i - 96 + 26 for i in range(97, 123)}

    for i in my_string:
        if i.isupper():
            answer[high_alphabet_dict[i]-1] += 1
        else:
            answer[low_alphabet_dict[i]-1] += 1
    return answer

# 다른 사람풀이1
def solution1(my_string):
    answer = [0] * 52
    for x in my_string:
        if x.upper():
            answer[ord(x)-65] += 1
        else:
            answer[ord(x)-71] += 1
    return answer

# 다른 사람풀이2
def solution2(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']