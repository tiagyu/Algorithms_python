# 첫 번째로 나오는 음수
def solution(num_list):
    for i in num_list:
        if i < 0:
            return num_list.index(i)
    return -1

# 다른 사람 풀이1
def solution1(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

# 다른 사람 풀이2
def solution2(num_list):
    return ([i for i in range(len(num_list)) if num_list[i] < 0] or [-1])[0]