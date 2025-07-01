# 2016년
def solution(a, b):
    weekday = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = 0
    for month in range(0, a):
        days += month_day[month]
    answer = weekday[(days + b - 1) % 7]
    return answer

# 다른 사람 풀이1
def solution2(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]

# 다른 사람 풀이2
import datetime

def solution3(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]