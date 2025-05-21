# 그림 확대
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

# 다른 사람 풀이1
def solution1(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.','.' * k).replace('x','x' * k))
    return answer

# 다른 사람 풀이2
def solution2(picture, k):
    answer = []
    for x in picture:
        temp = ''
        for y in x:
            temp += y * k
        for _ in range(k):
            answer.append(temp)
    return answer