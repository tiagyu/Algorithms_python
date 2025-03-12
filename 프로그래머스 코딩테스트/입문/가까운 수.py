# 가까운 수
def solution(array, n):
    # 빈 딕셔너리 생성
    blank_dict = {}
    
    # 딕셔너리 값 넣기
    for num in array:
        blank_dict[num] = abs(num - n) # 절대값 사용

    # 최소값 찾기
    min_value = min(blank_dict.values())

    # 최소값 value를 통해 key값 반환하기기
    find_key = [key for key, value in blank_dict.items() if value == min_value]
    
    # 절대값이 같은 경우 가장 가까운 값 찾기
    answer = sorted(find_key)[0]
    
    return answer

# 다른 사람 풀이 1
def solution2(array, n):
    array.sort(key = lambda x : (abs(x- n), x-n))
    answer = array[0]
    return answer

# 다른 사람 풀이 2
def solution3(array, n):
    array.sort()
    temp = []
    
    for i in array:
        temp.append(abs(n-i))
    
    return array[temp.index(min(temp))]