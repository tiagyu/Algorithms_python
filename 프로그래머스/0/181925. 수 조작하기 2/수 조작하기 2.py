def solution(numLog):
    num_dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        answer += num_dict[diff]
    return answer