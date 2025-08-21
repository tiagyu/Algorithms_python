def solution(myString, pat):
    mapping = str.maketrans({"A": "B", "B": "A"})
    myString = myString.translate(mapping)

    if pat in myString:
        return 1
    else:
        return 0