# 문자열 묶기
def solution(strArr):
    len_strArr = [len(i) for i in strArr]
    strArr_dict = {}
    for i in len_strArr:
        if i in strArr_dict:
            strArr_dict[i] += 1
        else:
            strArr_dict[i] = 1
    return max(strArr_dict.values())


# 다른 사람 풀이1
def solution1(strArr):
    a = [0] * 31
    for x in strArr:
        a[len(x)] += 1
    return max(a)


# 다른 사람 풀이2
def solution2(strArr):
    d = {}

    for i in strArr:
        # d에서 key 'i'를 찾되, 없으면 기본값 0을 사용한 뒤 1을 더한다.
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())
