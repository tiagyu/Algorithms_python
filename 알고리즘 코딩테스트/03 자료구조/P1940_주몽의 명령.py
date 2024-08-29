# 007 주몽의 명령
import sys

def method_1():
    n = int(input("Enter the value for n: "))
    M = int(input("Enter the value for M: "))
    grad = list(map(int, input("Enter the list of numbers: ").split()))

    grad.sort()  # 정렬
    count = 0
    start_index = 0
    end_index = n - 1

    while start_index < end_index:
        sum = grad[start_index] + grad[end_index]

        if sum == M:
            count += 1
            start_index += 1
            end_index -= 1  # 인덱스를 조정
        elif sum > M:
            end_index -= 1
        else:
            start_index += 1

    print(f"Method 1: {count}")


def method_2():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    i = 0
    j = N - 1

    while i < j:  # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
        if A[i] + A[j] < M:
            i += 1
        elif A[i] + A[j] > M:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1

    print(f"Method 2: {count}")


if __name__ == "__main__":
    print("Running Method 1:")
    method_1()
    print("\nRunning Method 2:")
    print("Note: For Method 2, please provide input through stdin (e.g., a file or redirected input).")
    # Uncomment the following line to run Method 2 directly if you're using an IDE or Jupyter notebook
    # method_2()
