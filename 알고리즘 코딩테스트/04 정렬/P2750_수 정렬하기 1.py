# 015 수 정렬하기 1
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())
    
for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            # 현재 A 리스트의 값보다 1칸 오른쪽 리스트의 값이 더 작으면 두 수 바꾸기
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])