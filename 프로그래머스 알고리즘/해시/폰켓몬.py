# 폰켓몬
def solution(nums):
    # 중복제거
    n = len(nums)
    nums = set(nums)
    print(nums)
    if len(nums) > n/2 :
        return print(len(nums)-1)
    else :
        return print(n/2)





solution([3,3,3,2,2,2])