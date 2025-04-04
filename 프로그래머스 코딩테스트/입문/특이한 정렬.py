# 특이한 정렬
def solution(numlist, n):
    dict = {}
    answer= []
    for num in numlist:
        dict[num] = abs(n - num)

    sorted_dict = sorted(dict.items(), key=lambda item : (item[1], -item[0]))

    for i in sorted_dict:
        answer.append(i[0])
    return answer

# 다른사람 풀이1
def solution1(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), n-x))
    return answer

# 다른사람 풀이2
def solution(numlist, n):
    numlist = [(abs(n-num), -num) for num in numlist]
    numlist.sort()
    return [-num for _, num in numlist]