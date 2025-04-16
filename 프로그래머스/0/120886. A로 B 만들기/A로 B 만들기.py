def solution(before, after):
    before_sort = sorted(before)
    after_sort = sorted(after)

    if before_sort == after_sort:
        return 1
    else:
        return 0