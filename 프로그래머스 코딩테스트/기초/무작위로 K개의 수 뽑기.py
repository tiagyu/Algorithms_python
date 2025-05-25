# 무작위로 K개의 수 뽑기
def solution(arr, k):
    answer = []
    for num in arr:
        if len(answer) < k and not num in answer:
            answer.append(num)

    while len(answer) < k:
        answer.append(-1)
    return answer

# 다른 사람 풀이1
def solution1(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break
    return ret + [-1] * (k - len(ret))

# 다른 사람 풀이2
def solution2(arr, k):
    res = list(dict.fromkeys(arr))
    res.extend([-1] * max(0, k-len(res)))
    return res[:k]