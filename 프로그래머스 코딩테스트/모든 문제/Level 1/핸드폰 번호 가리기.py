# 핸드폰 번호 가리기
def solution(phone_number):
    last_number = phone_number[-4:]
    answer = (len(phone_number)-4) * "*" + last_number
    return answer

# 다른 사람 풀이1
def solution1(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

# 다른 사람 풀이2
import re

def solution2(phone_number):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", phone_number, count = 0)