# 하샤드 수
def solution(x):
    num = sum(map(int, list(str(x))))

    if x % num:
        return False
    else:
        return True

# 다른 사람 풀이1
def solution1(x):
    return x%sum(int(x) for x in str(x)) == 0

# 다른 사람 풀이2
def solution2(x):
    st = str(x)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if x%a == 0 else False