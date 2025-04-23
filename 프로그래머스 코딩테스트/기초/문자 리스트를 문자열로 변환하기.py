# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = "".join(arr)
    return answer

# 다른 사람 풀이1
def solution1(arr):
    answer = ""
    for a in arr:
        answer += a
    return answer

# 다른 사람 풀이2
solution2 = lambda l: "".join(l)