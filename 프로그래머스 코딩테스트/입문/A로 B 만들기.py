# A로 B 만들기
def solution(before, after):
    before_sort = sorted(before)
    after_sort = sorted(after)

    if before_sort == after_sort:
        return 1
    else:
        return 0

# 다른 사람들 풀이1
def solution1(before, after):
    before = list(before)
    for i in after:
        try:
            del before[before.index(i)]
        except:
            return 0
    return 1