# 없는 숫자 더하기
def solution(numbers):
    all_num = [i for i in range(0,10)]
    diff = set(all_num) - set(sorted(numbers))
    return sum(diff)

# 다른 사람 풀이1
def solution1(numbers):
    return 45 - sum(numbers)

# 다른 사람 풀이2
def solution2(numbers):
    answer=0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer