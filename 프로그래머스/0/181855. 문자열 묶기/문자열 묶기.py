def solution(strArr):
    len_strArr = [len(i) for i in strArr]
    strArr_dict = {}
    for i in len_strArr:
        if i in strArr_dict:
            strArr_dict[i] += 1
        else:
            strArr_dict[i] = 1
    return max(strArr_dict.values())