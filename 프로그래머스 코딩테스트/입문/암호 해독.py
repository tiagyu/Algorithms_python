# 암호 해독
def solution(ciper, code):
    answer = ""
    new_ciper = "".join([" ",ciper])
    for i in range(1, len(new_ciper)):
        if i % code == 0 :
            answer += new_ciper[i]
    return answer

# 다른 사람 풀이 1
def solution1(ciper, code):
    answer = ciper[code-1::code]
    return answer

# 다른 사람 풀이 2
def solution2(ciper,code):
    answer = ""
    for i in range(code-1, len(ciper), code):
        answer += ciper[i]
    return answer