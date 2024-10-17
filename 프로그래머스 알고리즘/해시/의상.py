# 의상
def solution(clothes):
    
    # hash 생성
    hashDict = {}
    
    for _, category in clothes:
        if category in hashDict:
            hashDict[category] += 1
        else:
            hashDict[category] = 1
    
    # 조합 구하기
    answer = 1
    
    for _, value in hashDict.items():
        answer *= (value + 1)
        
    return answer - 1

print(solution([["yellow_hat", "headgear"], 
                ["blue_sunglasses", "eyewear"], 
                ["green_turban", "headgear"]]))