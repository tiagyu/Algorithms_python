def solution(number):
    answer = 0
    def get_combination(arr, r):
        result = []

        def find_combination(start_index, current_combination):
            # r개의 원소를 모두 선택했을 때
            if len(current_combination) == r:
                result.append(list(current_combination))  # 현재 조합을 결과에 추가
                return

            # 원소를 선택하는 재귀 호출
            for i in range(start_index, len(arr)):
                current_combination.append(arr[i])
                find_combination(i + 1, current_combination)
                current_combination.pop()  # 다음 초합을 위해 마지막 원소 제거

        find_combination(0, [])

        return result
    
    for i in get_combination(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer
