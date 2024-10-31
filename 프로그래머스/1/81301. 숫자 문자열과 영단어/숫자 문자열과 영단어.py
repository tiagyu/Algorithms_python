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