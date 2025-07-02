# 가운데 글자 가져오기
def solution(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2-1:len(s) // 2+1]
    
# 다른 사람 풀이1
def solution(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]