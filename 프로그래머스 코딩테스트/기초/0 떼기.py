# 0 떼기
def solution(n_str):
    return str(int(n_str))


# 다른 사람 풀이1
def solution1(n_str):
    return n_str.lstrip("0")


# 다른 사람 풀이2
def solution2(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]
