# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = [numbers[-1]] + numbers[:-1]
    else:
        answer = numbers[1:] + [numbers[0]]
    return answer

# 다른 사람들 풀이
def solutioin2(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == "right" else numbers[1:] + [numbers[0]]

# pop을 이용한 풀이
def solution3(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    return numbers