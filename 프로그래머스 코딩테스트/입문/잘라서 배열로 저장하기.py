# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = [my_str[i:i+n] for i in range(0, len(my_str),n)]
    return answer

# 다른 사람 풀이1
def solution1(my_str, n):
    answer = []
    
    while my_str:
        if len(my_str) >= n:
            answer.append(my_str[:n])
            my_str = my_str[n:]
        elif len(my_str) < n:
            answer.append(my_str)
            my_str = []
            
    return answer