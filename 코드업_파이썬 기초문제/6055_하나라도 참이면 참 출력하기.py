# 6055 하나라도 참이면 참 출력하기
a, b = map(int,input().split())
a = bool(a)
b = bool(b)
print(a or b)