# 한 번만 등장한 문자
def solution(s):
    s_list = []
    for i in list(s):
        if s.count(i) == 1:
            s_list.append(i)
    answer = "".join(sorted(s_list))
    return answer

# 다른 사람 풀이 1
def solution1(s):
    answer = "".join(sorted([ch for ch in s if s.count(ch) == 1]))
    return answer