# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = list(map(int,list(str(n))[::-1]))
    return answer

# 다른 사람 풀이1
def digit_reverse1(n):
    return list(map(int, reversed(str(n))))

# 다른 사람 풀이2
def digit_reverse2(n):
    return [int(i) for i in str(n)][::-1]