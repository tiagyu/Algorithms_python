# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = sorted(strings, key = lambda x : (x[n], x))
    return answer

# 다른 사람 풀이1
def solution1(strings, n):
    min = []
    result = []
    for i in strings:
        min.append(i[n])
        sorted_min = sorted(min)

    while len(result) != len(strings):
        for j in range(0, len(strings)):
            for k in range(0, len(strings)):
                if sorted_min[j] in strings[k][n]:
                    index = k
                    result.append(strings[index])
                    continue
    return result

# 다른 사람 풀이2
def solution2(strings, n):
    new =[]
    answer =[]
    for i in range(len(strings)):
        a = strings[i][n]
        b = a+strings[i]
        new.append(b)
    new.sort()
    for i in range(len(new)):
        c = new[i][1:]
        answer.append(c)
    return answer