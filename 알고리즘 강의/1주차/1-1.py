# 1. 문자열 팰린드롬 여부 확인
str = input()
if str == str[::-1]:
    print(True)
else:
    print(False)