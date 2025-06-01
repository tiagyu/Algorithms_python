def solution(my_string, is_suffix):
    suffix = []
    list_mystring = list(my_string)

    while len(list_mystring) > 0:
        suffix.append("".join(list_mystring))
        list_mystring.pop(0)
    if is_suffix in suffix:
        return 1
    return 0