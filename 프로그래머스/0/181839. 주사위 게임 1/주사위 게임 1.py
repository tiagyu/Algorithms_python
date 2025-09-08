def solution(a, b):
    odd_a = int(a % 2)
    odd_b = int(b % 2)
    if odd_a and odd_b:
        return (a**2 + b**2)
    elif odd_a or odd_b:
        return (2 * (a + b))
    else:
        return (abs(a - b))