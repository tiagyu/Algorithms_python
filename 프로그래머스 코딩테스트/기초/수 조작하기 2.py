# 수 조작하기 2
def solution(numLog):
    num_dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        answer += num_dict[diff]
    return answer

# 다른 사람 풀이1
def solution1(numLog):
    res = ''
    joystick = dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(numLog)):
        res += joystick[numLog[i]-numLog[i-1]]
    return res

# 다른 사람 풀이2
def solution2(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1] # 현재 값과 이전 값의 차이를 계산
        if diff == 1:
            answer += 'w' # 1 더하기
        elif diff == -1:
            answer += 's' # 1 빼기
        elif diff == 10:
            answer += 'd' # 10 더하기
        elif diff == -10:
            answer += 'a' # 10 빼기
    return answer