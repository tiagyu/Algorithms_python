# 002 평균구하기
def solution1():
    n = int(input())
    score = list(map(int,input().split()))

    M = max(score)
    sum = 0
    for i in score:
        sum+=(i / M * 100)

    answer = sum / n
    return print(answer)

def solution2():
    # 다른 풀이
    n = int(input())
    mylist = list(map(int, input().split()))
    mymax = max(mylist)
    mysum = sum(mylist)
    # 한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환해 로직을 간단하게 할 수 있음
    return print(mysum * 100 / mymax / int(n))

if __name__ == "__main__":
    # 첫 번째 풀이 실행
    print("첫 번째 풀이 결과:")
    solution1()

    # # 두 번째 풀이 실행
    # print("두 번째 풀이 결과:")
    # solution2()
