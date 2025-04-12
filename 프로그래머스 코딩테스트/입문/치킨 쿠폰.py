# 치킨 쿠폰
def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        service = coupon // 10
        answer += service
        coupon = service + (coupon % 10)

    return answer

# 다른 사람 풀이1
def solution1(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

# 다른 사람 풀이2
def solution2(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken,10)
        answer += chicken
        chicken += mod
    return answer