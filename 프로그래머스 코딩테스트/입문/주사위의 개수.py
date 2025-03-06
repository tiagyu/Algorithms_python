# 주사위의 개수
def solution(box, n):
    answer = 1
    # 가로
    width = box[0] // n
    
    # 세로
    depth = box[1] // n
     
    # 높이
    height = box[2] // n
    
    answer = width * depth * height
    return int(answer)

# 다른 사람들 풀이
def solution2(box, n):
    x, y, z = box
    return (x//n) * (y//n) * (z//n)

# for문을 이용한 풀이
def solution3(box, n):
    answer = 1
    for number in box:
        answer *= number // n
    return answer