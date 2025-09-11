# [PCCE 기출문제] 2번 / 각도 합치기
angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2 - (360 * ((angle1 + angle2) // 360))
print(sum_angle)

# 다른 사람 풀이1
angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2
print(sum_angle % 360)
