def solution(a, b):
    weekday = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = 0
    for month in range(0, a):
        days += month_day[month]
    answer = weekday[(days + b - 1) % 7]
    return answer