# 2. 중복 문자 없는 가장 긴 부분 문자열 찾기
def longest_unique_substring(s):
    char_index = {}
    start = max_length = 0

    for index, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = index
        max_length = max(max_length, index - start + 1)

    return max_length

s = input()
print(longest_unique_substring(s))
