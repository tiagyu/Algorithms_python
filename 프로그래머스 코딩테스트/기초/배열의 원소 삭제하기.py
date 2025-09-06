# 배열의 원소 삭제하기
def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr


# 다른 사람 풀이1
def solution1(arr, delete_list):

    return [i for i in arr if i not in delete_list]


# 다른 사람 풀이2
def solution2(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr
