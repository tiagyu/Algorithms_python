import re

def solution(order):
    americano = r'americano'
    latte = r'latte'
    answer = 0

    for i in order:
        if re.search(americano, i):
            answer += 4500
        elif re.search(latte, i):
            answer += 5000
        else:
            answer += 4500
    return answer