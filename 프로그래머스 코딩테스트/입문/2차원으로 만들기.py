# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    blank_list = []
    for i in num_list:
        blank_list.append(i)
        if len(blank_list) == n:
            answer.append(blank_list)
            blank_list = [] # 초기화
    return answer
    
# range를 잘 활용한 풀이
def solution2(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        print(i)
        answer.append(num_list[i:i+n])
    return answer

# numpy를 이용한 풀이
import numpy as np

def solution3(num_list, n):
    answer = np.array(num_list).reshape(-1,n)
    return answer.tolist()