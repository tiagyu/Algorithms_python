# 6045 정수 3개 입력받아 합과 평균 출력하기
a, b, c = map(int,input().split())
d = a + b + c
e = d/3
print(d,format(e,'.2f'))