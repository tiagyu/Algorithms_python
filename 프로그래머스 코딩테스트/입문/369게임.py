# 369게임
def solution(order):
    answer = 0
    for i in str(order):
        if int(i) % 3 == 0 and not int(i) == 0:
            answer +=1
    return answer

# 다른 사람 풀이 1
def solution2(order):
    return sum(map(lambda x : str(order).count(str(x)), [3,6,9]))

# 다른 사람 풀이 2
def solution3(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')