def solution(myStr):
    mapping = str.maketrans({"a": " ", "b": " ", "c": " "})
    myStr = myStr.translate(mapping)
    if myStr.split():
        return myStr.split()
    else:
        return ["EMPTY"]
