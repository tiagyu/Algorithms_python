# k의 개수
def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        num_list = list(str(num))
        for nl in num_list:
            if nl == str(k):
                answer += 1
    return answer

# 다른 사람 풀이1
def solution1(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i,j+1)])
    return answer

# 다른 사람 풀이2
def solution2(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer += str(n).count(str(k))
    return answer