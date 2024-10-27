from collections import Counter

def solution(nums):
    nums_counter = Counter(nums)
    return min(len(nums_counter), len(nums)//2)