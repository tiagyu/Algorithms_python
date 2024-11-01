# 폰켓몬
# 1. 중복제거

def solution1(nums):
    # n 설정
    n = len(nums)
    
    # 중복제거
    nums = set(nums)
    
    # 중복 제거한 nums의 길이가 n//2 보다 크면 n//2 경우의 수 가능
    if len(nums) > n//2 :
        return n//2
    else :
        return len(nums)

print('Sol 1 :', solution1([3,1,2,3]))

# 2. hash 사용

def solution2(nums):
    hasDict = {}
    
    # 1. nums list의 hash를 구한다
    for n in nums:
        if n in hasDict:
            hasDict[n] += 1
        else:
            hasDict[n] = 1
    
    # n//2 마리를 가질 수 있음
    max_pokemons = len(nums) // 2
    
    return min(len(hasDict), max_pokemons)

print('Sol 2 :', solution2([3,1,2,3]))

# 3. Counter를 활용
from collections import Counter

def solution3(nums):
    nums_counter = Counter(nums)
    return min(len(nums_counter), len(nums)//2)

print('Sol 3 :', solution3([3,1,2,3]))