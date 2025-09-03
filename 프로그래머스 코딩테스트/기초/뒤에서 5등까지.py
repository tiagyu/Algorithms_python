# 뒤에서 5등까지
def solution(num_list):
    return sorted(num_list)[:5]


# 다른 사람 풀이1
def solution1(num_list):
    answer = []
    for i in range(5):

        answer.append(min(num_list))
        num_list.remove(min(num_list))
    return answer


# 다른 사람 풀이2
solution = lambda num_list: sorted(num_list)[:5]
