# 홀짝 구분하기
n = int(input())

if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
    
# 다른 사람 풀이1
n = int(input())
print(f"{n} is {'even' if n % 2==0 else 'odd'}")