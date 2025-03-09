# 문자열 정렬하기 (1)
def solution(my_string):
    answer = []
    number = "0123456789"

    for i in my_string:
        if i in number:
            print(i)
            answer.append(int(i))
    answer.sort()
    return answer

# 다른 사람 풀이1
def solution2(my_string):
    answer = []
    for i in my_string:
        if i.isdigit(): # isdigit 사용
            answer.append(int(i))
    answer.sort()
    return answer

# 다른 사람 풀이2
def solution3(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])