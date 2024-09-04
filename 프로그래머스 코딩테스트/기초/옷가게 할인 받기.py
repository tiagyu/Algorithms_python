# 옷가게 할인 받기
def solution(price):
    discount = 1
    if 300000 > price >= 100000:
        discount = 0.95
    elif 500000 > price >= 300000:
        discount = 0.9
    elif price >= 500000:
        discount = 0.8

    answer = int(price * discount)
    return answer

print(solution(150000))