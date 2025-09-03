# 뒤에서 5등 위로
def solution(num_list):
    return sorted(num_list)[5:]


# 다른 사람 풀이1
def solution1(num_list):
    num_list.sort()
    answer = num_list[5:]
    return answer


# 다른 사람 풀이2
def solution2(num_list):
    num_list.sort()
    return num_list[5:]
