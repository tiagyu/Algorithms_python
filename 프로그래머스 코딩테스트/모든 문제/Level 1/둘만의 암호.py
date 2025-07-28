# 둘만의 암호
def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

    for ch in skip:
        if ch in alphabet:
            alphabet.remove(ch)
        
    alphabet *= 2

    for ch in s:
        cur_idx = alphabet.index(ch)
        new_idx = (cur_idx + index) % len(alphabet)
        answer += alphabet[new_idx]

    return answer

# 다른 사람 풀이1
from string import ascii_lowercase

def solution1(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result

# 다른 사람 풀이2
def solution2(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    ans = ''
    for i in s:
        ans += atoz[(atoz.index(i)+index)%len(atoz)]

    return ans