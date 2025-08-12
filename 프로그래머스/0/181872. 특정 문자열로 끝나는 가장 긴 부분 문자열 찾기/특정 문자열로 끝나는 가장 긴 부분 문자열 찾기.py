def solution(myString, pat):
    idx = len(myString) -len(pat) - (myString[::-1].index(pat[::-1]))
    return myString[:idx+len(pat)]