# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2: #파이썬에서 0이 아닌 모든 숫자는 True로 평가된다
        print('-',end='') #홀수인 경우 - 출력
    else:
        print('+',end='') #짝수인 경우 + 출력
        
print()