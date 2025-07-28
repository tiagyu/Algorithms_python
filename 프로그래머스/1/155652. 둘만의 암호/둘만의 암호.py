def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

    for ch in skip:
        if ch in alphabet:
            alphabet.remove(ch)

    for ch in s:
        cur_idx = alphabet.index(ch)
        new_idx = (cur_idx + index) % len(alphabet)
        answer += alphabet[new_idx]

    return answer