# 모스부호 (1)
def solution(letter):
    answer = ''
    
    # 모스부호 딕셔너리
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    # letter 나누기(공백 기준)
    letter = str(letter).split()
    
    # 딕셔너리 비교
    for alphabet in letter:
        for key, value in morse.items():
            if alphabet == key:
                answer += value
    
    return answer

# 딕셔너리 인덱스 개념 적용
def solution2(letter):
    answer = ''
    
    # 모스부호 딕셔너리
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    split_letter = letter.split()
    for index in split_letter:
        answer += morse[index]
        
    return answer