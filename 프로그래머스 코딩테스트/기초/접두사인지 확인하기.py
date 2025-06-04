# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[:i+1])

    if is_prefix in answer:
        return 1
    return 0

# 다른 사람 풀이1
def solution1(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

# 다른 사람 풀이2
def solution2(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix: return 1
    return 0

# 다른 사람 풀이3
def solution3(my_string, is_prefix):
    return 1 if my_string.find(is_prefix) == 0 else 0