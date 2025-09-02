# 배열 비교하기
def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1


# 다른 사람 풀이1
def solution1(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (
        sum(arr1) > sum(arr2)
    ) - (sum(arr2) > sum(arr1))


# 다른 사람 풀이2
def solution2(arr1, arr2):
    x, y = len(arr1), len(arr2)
    if x != y:
        return 1 if x > y else -1
    elif x == y:
        sum_x, sum_y = sum(arr1), sum(arr2)
        if sum_x > sum_y:
            return 1
        elif sum_x < sum_y:
            return -1
        else:
            return 0
