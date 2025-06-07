# qr code
def solution(q, r, code):
    answer = ''
    for i in range(r,len(code),q):
        answer += code[i]
    return answer

# 다른 사람풀이1
def solution1(q, r, code):
    return code[r::q]

# 다른 사람풀이2
def solution2(q, r, code):
    return ''.join(code[i] for i in range(r, len(code), q))