# 옹알이 (1)
def solution(babbling):
    answer = 0
    babbling_list = [
    'aya',"ye",'woo',"ma"
    ]

    for i in babbling:
        for j in babbling_list:
            if i.count(j) == 1:
                i = i.split(j)
                i = ",".join(i)
        i = i.replace(",","")
        if len(i) == 0:
            answer += 1
    return answer

# 다른 사람 풀이1
import re

def solution1(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt = 0
    for e in babbling:
        if regex.match(e):
            cnt += 1
    return cnt

# 다른 사람 풀이2
def solution2(babbling):
    c = 0
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            if w * 2 not in b:
                b = b.replace(w," ",1)
        if len(b.strip()) == 0:
            c += 1
    return c