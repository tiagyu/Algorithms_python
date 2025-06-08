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