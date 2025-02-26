# 외계행성의 나이
def solution(age):
    # 지정값 딕셔너리로 입력
    age_dict = {
        "a" : "0",
        "b" : "1",
        "c" : '2',
        "d" : '3',
        "e" : '4',
        "f" : '5',
        "g" : '6',
        "h" : '7',
        "i" : '8',
        "j" : '9'
    }
    # 입력값 age 문자열로 변환
    age = str(age)
    
    # 빈 문자열 생성
    answer = ""

    # 딕셔너리에서 해당 문자열 찾기
    for i in age:
        for alpha, num in age_dict.items():
            if i == num:
                answer += alpha

    return str(answer)

# 리스트 인덱스를 사용
def solution2(age):
    answer = ""
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    for i in age:
        answer += alpha[int(i)]
    return answer

print(solution2(35))