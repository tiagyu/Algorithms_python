def solution(myString, pat):
    count = 0

    for i in range(0, len(myString) - len(pat) + 1):
        print(myString[i:i+len(pat)])
        if myString[i:i+len(pat)] == pat:
            count += 1
    return count