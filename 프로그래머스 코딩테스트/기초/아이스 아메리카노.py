# 아이스 아메리카노
def solution(money):
    array = []
    price = 5500
    num = money // price
    change = money - (price * num)
    array.append(num)
    array.append(change)
    return array

def solution2(money):
    answer = [money // 5500, money % 5500]
    return answer

print(solution(15000))