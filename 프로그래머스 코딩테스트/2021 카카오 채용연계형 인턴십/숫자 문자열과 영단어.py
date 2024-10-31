# 숫자 문자열과 영단어
def solution(s):
    answer = ''
    number = '1234567890'
    letter = ''
    
    for i in s:
        if i in number:
            answer += i
        else:
            letter += i
        
            if letter == 'one':
                answer += '1'
                letter = ''
            elif letter == 'two':
                answer += '2'
                letter = ''
            elif letter == 'three':
                answer += '3'
                letter = ''
            elif letter == 'four':
                answer += '4'
                letter = ''             
            elif letter == 'five':
                answer += '5'
                letter = ''
            elif letter == 'six':
                answer += '6'
                letter = ''
            elif letter == 'seven':
                answer += '7'
                letter = ''
            elif letter == 'eight':
                answer += '8'
                letter = ''
            elif letter == 'nine':
                answer += '9'
                letter = ''
            elif letter == 'zero':
                answer += '0'
                letter = ''      
        
    return int(answer)

print(solution("one4seveneight"))

num_dcit = {'zero' : '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
            'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine': '9'}

# 딕셔너리를 이용한 풀이
def solution2(s):
    answer = s
    for key, value in num_dcit.items():
        answer = answer.replace(key,value)
    return int(answer)

print(solution2("one4seveneight"))

# replace 이용
def solution3(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(words)):
        s = s.replace(words[i], str(i))
    return int(s)

print(solution3("one4seveneight"))