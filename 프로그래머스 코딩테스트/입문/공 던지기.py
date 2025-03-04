# 공 던지기
def solution(numbers, k):
    answer = []
    if len(numbers) % 2 == 0:
        for i in numbers:
            if i % 2 != 0:
                answer.append(i)
    else:
        for i in numbers:
            if i % 2 != 0:
                answer.append(i)
        for i in numbers:
            if i % 2 == 0:
                answer.append(i)
    
    # k 변수 고려
    if len(answer) < k:
        answer = answer * k

    return answer[k-1]

# 효율적인 코드
def solution2(numbers, k):
    return numbers[ 2 * (k-1) % len(numbers)]