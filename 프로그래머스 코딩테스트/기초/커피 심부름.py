# 커피 심부름
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

# 다른 사람 풀이1
def solution1(order):
    answer = 0
    for want in order:
        if 'latte' in want:
            answer += 5000
        answer += 4500
    return answer

# 다른 사람 풀이2
def solution2(order):
    return sum([5000 if "cafelatte" in i else 4500 for i in order])