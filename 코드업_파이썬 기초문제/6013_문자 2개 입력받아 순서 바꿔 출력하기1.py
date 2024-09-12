# 6013 문자 2개 입력받아 순서 바꿔 출력하기1
n = 2
array = []
for i in range(n):
    a = input()
    array.append(a)

for char in array[::-1]:
    print(char)