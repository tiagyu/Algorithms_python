# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    idx = len(myString) -len(pat) - (myString[::-1].index(pat[::-1]))
    return myString[:idx+len(pat)]

# 다른 사람 풀이1
def solution1(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

# 다른 사람 풀이2
def solution2(myString, pat):
    return myString[:myString.rfind(pat) + len(pat)]