def solution(picture, k):
    answer = []
    for pic in picture:
        pic_list = list(pic)
        answer_letter = ""
        for letter in pic_list:
            answer_letter += letter * k
        for _ in range(k):
            answer.append(answer_letter)
    return answer