# 003 구간 합 구하기1
def solution1():
    # 첫 번째 풀이
    n, q = map(int, input().split())  # n: 배열의 크기, q: 쿼리 수
    array = list(map(int, input().split()))  # 배열 입력 받기
    sum_array = [0]
    total = 0

    # 구간 합 배열 생성
    for k in array:
        total += k
        sum_array.append(total)

    # 쿼리 처리
    for _ in range(q):
        i, j = map(int, input().split())
        print(sum_array[j] - sum_array[i - 1])


def solution2():
    # 두 번째 풀이
    import sys
    input = sys.stdin.readline  # 빠른 입력 처리
    suNo, quizNo = map(int, input().split())  # suNo: 배열의 크기, quizNo: 쿼리 수
    numbers = list(map(int, input().split()))  # 배열 입력 받기
    prefix_sum = [0]
    temp = 0

    # 구간 합 배열 생성
    for i in numbers:
        temp += i
        prefix_sum.append(temp)

    # 쿼리 처리
    for _ in range(quizNo):
        s, e = map(int, input().split())
        print(prefix_sum[e] - prefix_sum[s - 1])


if __name__ == "__main__":
    # 첫 번째 풀이 실행
    print("첫 번째 풀이 결과:")
    solution1()

    # 두 번째 풀이 실행
    # print("두 번째 풀이 결과:")
    # solution2()
